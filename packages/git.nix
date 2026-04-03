{
  lib,
  pkgs,
  ...
}:

pkgs.stdenv.mkDerivation rec {
  pname = "obsidian.plugins.git";
  version = "2.38.0";
  repo = "https://github.com/Vinzent03/obsidian-git";

  mainJs = pkgs.fetchurl {
    url = "${repo}/releases/download/${version}/main.js";
    sha256 = "sha256-tWiDV6CUDrzFy9+y9faM4UGQAaZBtqG9xQX2E9R0MLI=";
  };

  manifest = pkgs.fetchurl {
    url = "${repo}/releases/download/${version}/manifest.json";
    sha256 = "sha256-TUjIYfxZPoPa/b6L+TbJ9i4XxVmmdlvU/d3hmylPoxM=";
  };

  stylesCss = pkgs.fetchurl {
    url = "${repo}/releases/download/${version}/styles.css";
    sha256 = "sha256-CTj/FgBO4fM2JyiZHijc4LuTe+USRtoIKWOAA1N76q4=";
  };

  phases = [ "installPhase" ];

  installPhase = ''
    mkdir -p $out
    cp $mainJs $out/main.js
    cp $manifest $out/manifest.json
    cp $stylesCss $out/styles.css
  '';
}