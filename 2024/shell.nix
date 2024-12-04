with import <nixpkgs> { };

let
  p = python3Packages;
in
pkgs.mkShell rec {
  name = "aoc";
  venvDir = "./.venv";
  buildInputs = [
    p.python
    p.venvShellHook
  ];

  postVenvCreation = ''
    unset SOURCE_DATE_EPOCH
  '';

  postShellHook = ''
    unset SOURCE_DATE_EPOCH
    alias v=nvim
  '';
}
