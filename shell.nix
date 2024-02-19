let
  nixpkgs = fetchTarball "https://github.com/NixOS/nixpkgs/tarball/nixos-23.11";
  pkgs = import nixpkgs { config = {}; overlays = []; };
in
pkgs.mkShell {
  packages = [
    pkgs.python3
    pkgs.python311Packages.pyparsing
    pkgs.python311Packages.pyyaml
    pkgs.python311Packages.tqdm
    pkgs.python311Packages.pebble

    pkgs.gcc13
    pkgs.dotnet-sdk_8
    pkgs.go
    pkgs.jdk21
    pkgs.nodejs_21
    pkgs.kotlin
    pkgs.php83
    pkgs.ruby_3_3
    pkgs.rustc
    pkgs.scala_3
  ];
}