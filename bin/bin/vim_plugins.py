#!/usr/bin/env python3

import os
import sys
import argparse
import subprocess
from pathlib import Path

parser = argparse.ArgumentParser(description="Manage Vim plugins")
parser.add_argument("what", help="Manage bundle", choices=["init", "update"])

plugins = {
        "a": "https://github.com/vim-scripts/a.vim.git",
        "ack": "https://github.com/mileszs/ack.vim.git",
        "ale": "https://github.com/dense-analysis/ale.git",
        "auto-pairs": "https://github.com/jiangmiao/auto-pairs.git",
        "bookmarks": "https://github.com/MattesGroeger/vim-bookmarks.git",
        "bufexplorer": "https://github.com/jlanzarotta/bufexplorer.git",
        "deoplete": "https://github.com/Shougo/deoplete.nvim.git",
        "dirvish": "https://github.com/justinmk/vim-dirvish.git",
        "dispatch": "https://github.com/tpope/vim-dispatch.git",
        "easymotion": "https://github.com/easymotion/vim-easymotion.git",
        "everforest": "https://github.com/sainnhe/everforest.git",
        "fugitive": "https://github.com/tpope/vim-fugitive.git",
        "gitgutter": "https://github.com/airblade/vim-gitgutter.git",
        "javascript": "https://github.com/pangloss/vim-javascript.git",
        "jedi-vim": "https://github.com/davidhalter/jedi-vim.git",
        "lualine": "https://github.com/nvim-lualine/lualine.nvim.git",
        "misc": "https://github.com/xolox/vim-misc.git",
        "nerdcommenter": "https://github.com/scrooloose/nerdcommenter.git",
        "plenary": "https://github.com/nvim-lua/plenary.nvim.git",
        "rainbow": "https://github.com/luochen1990/rainbow",
        "sensible": "https://github.com/tpope/vim-sensible.git",
        "session": "https://github.com/xolox/vim-session.git",
        "sneak": "https://github.com/justinmk/vim-sneak.git",
        "snippets": "https://github.com/honza/vim-snippets.git",
        "speeddating": "https://github.com/tpope/vim-speeddating.git",
        "surround": "https://github.com/tpope/vim-surround.git",
        "tabular": "https://github.com/godlygeek/tabular.git",
        "tagbar": "https://github.com/majutsushi/tagbar.git",
        "telescope": "https://github.com/nvim-telescope/telescope.nvim.git",
        "ultisnips": "https://github.com/SirVer/ultisnips.git"
        }


if __name__ == "__main__":

    args = parser.parse_args()

    if os.name == "nt":
        bundle_dir = Path.home() / "Neovim" / "share" / "nvim" / "runtime" / "pack" / "plugins" / "start"
    else:
        bundle_dir = Path.home() / ".vim" / "pack" / "plugins" / "start"

    if args.what == "update":
        for plug_dir in bundle_dir.iterdir():
            print("* Updating {}".format(plug_dir.name))
            print(subprocess.check_output(
                ["git", "pull", "--recurse-submodules"],
                text=True,
                stderr=subprocess.STDOUT,
                cwd=plug_dir))

    elif args.what == "init":
        bundle_dir.mkdir(parents=True, exist_ok=True)
        if len(list(bundle_dir.iterdir())):
            print("Bundle directory is not empty")
            sys.exit(1)

        for plug, url in plugins.items():
            print("* Installing {}".format(plug))
            subprocess.run(
                ["git", "clone", "--verbose", "--recursive", url, plug],
                text=True,
                check=True,
                cwd=bundle_dir)


