#!/bin/sh

cd $HOME/Programme/neovim
make CMAKE_INSTALL_PREFIX=$HOME/.local CMAKE_BUILD_TYPE=Release
make install
