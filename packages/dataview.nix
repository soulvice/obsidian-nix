{
  lib,
  pkgs,
  ...
}:

pkgs.stdenv.mkDerivation rec {
  pname = "obsidian.plugins.dataview";
  version = "0.5.70";
  repo = "https://github.com/blacksmithgu/obsidian-dataview";

  mainJs = pkgs.fetchurl {
    url = "${repo}/releases/download/${version}/main.js";
    sha256 = "sha256-a7HPcBCvrYMOc1dfyg4r+9MnnFYuPZ0k8tL0UWHrfQA=";
  };

  manifest = pkgs.fetchurl {
    url = "${repo}/releases/download/${version}/manifest.json";
    sha256 = "sha256-kjXbRxEtqBuFWRx57LmuJXTl5yIHBW6XZHL5BhYoYYU=";
  };

  stylesCss = pkgs.fetchurl {
    url = "${repo}/releases/download/${version}/styles.css";
    sha256 = "sha256-MwbdkDLgD5ibpyM6N/0lW8TT9DQM7mYXYulS8/aqHek=";
  };

  phases = [ "installPhase" ];

  installPhase = ''
    mkdir -p $out
    cp $mainJs $out/main.js
    cp $manifest $out/manifest.json
    cp $stylesCss $out/styles.css
  '';
}