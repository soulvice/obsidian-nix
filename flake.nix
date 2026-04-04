{
  description = "Nix packages for all Obsidian community plugins and themes";

  inputs.nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";

  outputs =
    { self, nixpkgs }:
    let
      systems = [
        "x86_64-linux"
        "aarch64-linux"
        "x86_64-darwin"
        "aarch64-darwin"
      ];

      lib = nixpkgs.lib;
      forAllSystems = lib.genAttrs systems;

      pluginsData = builtins.fromJSON (builtins.readFile ./plugins-data.json);
      themesData = builtins.fromJSON (builtins.readFile ./themes-data.json);

      # Build a plugin derivation from a plugins-data.json entry.
      # Fetches main.js, manifest.json, and optionally styles.css from GitHub releases.
      mkPlugin =
        pkgs: id: plugin:
        let
          hasStyles = plugin ? stylesCss;
          base = "https://github.com/${plugin.repo}/releases/download/${plugin.version}";

          files =
            {
              mainJs = pkgs.fetchurl {
                url = "${base}/main.js";
                sha256 = plugin.mainJs;
              };
              manifest = pkgs.fetchurl {
                url = "${base}/manifest.json";
                sha256 = plugin.manifest;
              };
            }
            // lib.optionalAttrs hasStyles {
              stylesCss = pkgs.fetchurl {
                url = "${base}/styles.css";
                sha256 = plugin.stylesCss;
              };
            };
        in
        pkgs.stdenv.mkDerivation (
          files
          // {
            pname = "obsidian-plugin-${id}";
            inherit (plugin) version;

            phases = [ "installPhase" ];

            installPhase =
              ''
                mkdir -p $out
                cp $mainJs $out/main.js
                cp $manifest $out/manifest.json
              ''
              + lib.optionalString hasStyles ''
                cp $stylesCss $out/styles.css
              '';
          }
        );

      # Build a theme derivation from a themes-data.json entry.
      # Clones the full repo (fetchFromGitHub) and copies manifest.json + theme.css.
      mkTheme =
        pkgs: id: theme:
        let
          repoParts = lib.splitString "/" theme.repo;
          owner = builtins.head repoParts;
          repoName = builtins.elemAt repoParts 1;
        in
        pkgs.stdenv.mkDerivation {
          pname = "obsidian-theme-${id}";
          version = theme.rev;

          src = pkgs.fetchFromGitHub {
            inherit owner;
            repo = repoName;
            rev = theme.rev;
            hash = theme.hash;
          };

          phases = [ "installPhase" ];

          installPhase = ''
            mkdir -p $out
            cp $src/manifest.json $out/manifest.json
            cp $src/theme.css $out/theme.css
          '';
        };
    in
    {
      # Standard flake packages — useful for `nix build .#plugin.dataview` etc.
      packages = forAllSystems (
        system:
        let
          pkgs = nixpkgs.legacyPackages.${system};
        in
        {
          plugin = lib.mapAttrs (mkPlugin pkgs) pluginsData;
          theme  = lib.mapAttrs (mkTheme pkgs) themesData;
        }
      );

      # Overlay — the ergonomic way to consume plugins/themes without spelling out ${system}.
      # Add to nixpkgs.overlays in your NixOS or home-manager config, then use:
      #
      #   with pkgs.obsidianPlugins; [ dataview templater-obsidian ]
      #   with pkgs.obsidianThemes;  [ catppuccin ]
      #
      # Note: pkgs.obsidian (the app) already exists in nixpkgs — these are intentionally
      # named obsidianPlugins / obsidianThemes to avoid that collision.
      overlays.default = final: _prev: {
        obsidianPlugins = lib.mapAttrs (mkPlugin final) pluginsData;
        obsidianThemes  = lib.mapAttrs (mkTheme final) themesData;
      };

      # Library functions — build a one-off plugin or theme that isn't in the community list.
      # Useful for private repos, forks, or unreleased plugins.
      #
      # mkPlugin example:
      #   inputs.obsidian-nix.lib.mkPlugin pkgs {
      #     id       = "my-private-plugin";
      #     repo     = "myorg/obsidian-my-plugin";   # "owner/repo" on GitHub
      #     version  = "1.0.0";
      #     mainJs   = "sha256-...";
      #     manifest = "sha256-...";
      #     # stylesCss = "sha256-...";              # optional
      #   }
      #
      # mkTheme example:
      #   inputs.obsidian-nix.lib.mkTheme pkgs {
      #     id   = "my-private-theme";
      #     repo = "myorg/obsidian-my-theme";
      #     rev  = "1.0.0";                          # tag or commit SHA
      #     hash = "sha256-...";                     # hash of the unpacked repo archive
      #   }
      #
      # Tip — get the hash without guessing:
      #   nix store prefetch-file --unpack --hash-type sha256 \
      #     https://github.com/myorg/obsidian-my-theme/archive/1.0.0.tar.gz
      lib = {
        mkPlugin = pkgs: { id, ... }@args: mkPlugin pkgs id (lib.removeAttrs args [ "id" ]);
        mkTheme  = pkgs: { id, ... }@args: mkTheme  pkgs id (lib.removeAttrs args [ "id" ]);
      };
    };
}
