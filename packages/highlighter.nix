{
  lib,
  pkgs,
  ...
}:

pkgs.stdenv.mkDerivation rec {
  pname = "obsidian.plugins.highlightr";
  version = "1.2.2";
  repo = "https://github.com/chetachiezikeuzor/Highlightr-Plugin";

  mainJs = pkgs.fetchurl {
    url = "${repo}/releases/download/${version}/main.js";
    sha256 = "sha256-/UMn89adcvwQk2qhKvUboZUkjbOmLqsM4z1uyb2wu40=";
  };

  manifest = pkgs.fetchurl {
    url = "${repo}/releases/download/${version}/manifest.json";
    sha256 = "sha256-LBshxhr9jr6s02V3RVPkLTF/NyqMRfB7kwkJ5FH3h6M=";
  };

  stylesCss = pkgs.fetchurl {
    url = "${repo}/releases/download/${version}/styles.css";
    sha256 = "sha256-b90+UvffP/SnQpfTRvtIMjCUBtKqBh98ncElkcuJpy8=";
  };

  phases = [ "installPhase" ];

  installPhase = ''
    mkdir -p $out
    cp $mainJs $out/main.js
    cp $manifest $out/manifest.json
    cp $stylesCss $out/styles.css
  '';
}