{
  lib,
  pkgs,
  ...
}:

pkgs.stdenv.mkDerivation rec {
  pname = "obsidian.plugins.calendar";
  version = "2.0.0-beta.2";
  repo = "https://github.com/liamcain/obsidian-calendar-plugin";

  mainJs = pkgs.fetchurl {
    url = "${repo}/releases/download/${version}/main.js";
    sha256 = "sha256-ZNHGxiCAMkZyS8kixcLgoXxAb/wj9rvPv7FMZDlY+7c=";
  };

  manifest = pkgs.fetchurl {
    url = "${repo}/releases/download/${version}/manifest.json";
    sha256 = "sha256-MU/BeSmiJwsX6jklOO4tkzMHFIAOJEspdbbBn5uNxok=";
  };

  stylesCss = pkgs.fetchurl {
    url = "${repo}/releases/download/${version}/styles.css";
    sha256 = "sha256-SGtFAHbzQ5ueQIU2ZaP1HlCEyrpguILChbYPR2TCCFI=";
  };

  phases = [ "installPhase" ];

  installPhase = ''
    mkdir -p $out
    cp $mainJs $out/main.js
    cp $manifest $out/manifest.json
    cp $stylesCss $out/styles.css
  '';
}