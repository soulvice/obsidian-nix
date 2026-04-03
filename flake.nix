{
  description = "A flake providing a collection of obsidian plugins";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
  };

  outputs =
    { self, nixpkgs }:
    let
      system = "x86_64-linux";
      pkgs = nixpkgs.legacyPackages.${system};
      lib = nixpkgs.lib;
    in
    {
      packages.${system} = let
        dir = builtins.readDir ./packages;
        nixFiles = lib.filterAttrs (name: type:
          type == "regular" && lib.hasSuffix ".nix" name
        ) dir;
      in 
        map (name: pkgs.callPackage ./packages/${name} {}) (builtins.attrNames nixFiles);

      checks.${system} = self.packages.${system};
    };
}