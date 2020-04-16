#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import argparse
import subprocess

parser = argparse.ArgumentParser(description="Manage Vim plugins")
parser.add_argument("what", help="Manage bundle", choices=["init", "update"])

plugins = {
        "a":"https://github.com/vim-scripts/a.vim.git",
        "ack":"https://github.com/mileszs/ack.vim.git",
        "ale":"git clone https://github.com/dense-analysis/ale.git",
        "auto-pairs":"https://github.com/jiangmiao/auto-pairs.git",
        "bookmarks":"https://github.com/MattesGroeger/vim-bookmarks.git",
        "bufexplorer":"https://github.com/jlanzarotta/bufexplorer.git",
        # "ctrlp":"https://github.com/ctrlpvim/ctrlp.vim.git",
        "denite":"https://github.com/Shougo/denite.nvim.git",
        "deoplete":"https://github.com/Shougo/deoplete.nvim.git",
        "dirvish":"https://github.com/justinmk/vim-dirvish.git",
        "dispatch":"https://github.com/tpope/vim-dispatch.git",
        "easymotion":"https://github.com/easymotion/vim-easymotion.git",
        "fugitive":"https://github.com/tpope/vim-fugitive.git",
        "gitgutter":"https://github.com/airblade/vim-gitgutter.git",
        "gundo":"https://github.com/sjl/gundo.vim.git",
        "is":"https://github.com/haya14busa/is.vim.git",
        "javascript":"https://github.com/pangloss/vim-javascript.git",
        "jedi-vim":"https://github.com/davidhalter/jedi-vim.git",
        "misc":"https://github.com/xolox/vim-misc.git",
        "nerdcommenter":"https://github.com/scrooloose/nerdcommenter.git",
        "rainbow":"https://github.com/junegunn/rainbow_parentheses.vim.git",
        "sensible":"https://github.com/tpope/vim-sensible.git",
        "session":"https://github.com/xolox/vim-session.git",
        "sneak":"https://github.com/justinmk/vim-sneak.git",
        "snippets":"https://github.com/honza/vim-snippets.git",
        "speeddating":"https://github.com/tpope/vim-speeddating.git",
        "surround":"https://github.com/tpope/vim-surround.git",
        "tabular":"https://github.com/godlygeek/tabular.git",
        "tagbar":"https://github.com/majutsushi/tagbar.git",
        "tern":"https://github.com/ternjs/tern_for_vim.git",
        "ultisnips":"https://github.com/SirVer/ultisnips.git",
        # "unimpaired":"https://github.com/tpope/vim-unimpaired.git",
        # "unite":"https://github.com/Shougo/unite.vim.git",
        # "unite-outline":"https://github.com/Shougo/unite-outline.git",
        "vim-colors-solarized":"https://github.com/altercation/vim-colors-solarized.git",
        }


if __name__ == "__main__":

    args = parser.parse_args()

    if os.name == "nt":
        bundle = os.path.join(os.path.expanduser("~"), "Neovim", "share", "nvim", "runtime", "bundle")
    else:
        bundle = os.path.join(os.path.expanduser("~"), ".vim", "bundle")

    os.chdir(bundle)

    installed_plugins = os.listdir(bundle)

    if args.what == "update":
        for p in installed_plugins:

            print("* Updating {}".format(p))
            print(subprocess.check_output(
                ["git", "pull"],
                text=True,
                stderr=subprocess.STDOUT,
                cwd=os.path.join(bundle, p)))

    elif args.what == "init":
        if len(installed_plugins):
            print("Bundle directory is not empty")
            sys.exit(1)

        for plug, url in plugins.items():
            print("* Updating {}".format(plug))
            subprocess.run(
                ["git", "clone", "--verbose", "--recursive", url, plug],
                text=True,
                check=True,
                cwd=bundle)


