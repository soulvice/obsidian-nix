{
  lib,
  pkgs,
  ...
}:

pkgs.stdenv.mkDerivation rec {
  pname = "obsidian.theme.catppuccin";
  version = "2.0.3";

  src = pkgs.fetchFromGitHub {
    owner = "catppuccin";
    repo = "obsidian";
    rev = version;
    hash = "sha256-AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA=";
  };

  phases = [ "installPhase" ];

  installPhase = ''
    mkdir -p $out
    cp -r $src/* $out/
  '';
}