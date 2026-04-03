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
      packages = forAllSystems (
        system:
        let
          pkgs = nixpkgs.legacyPackages.${system};
        in
        lib.mapAttrs (mkPlugin pkgs) pluginsData
        // lib.mapAttrs (mkTheme pkgs) themesData
      );
    };
}
