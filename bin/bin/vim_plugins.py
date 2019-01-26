#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import argparse
import subprocess

parser = argparse.ArgumentParser(description="Manage Vim plugins")
parser.add_argument("what", help="Manage bundle", choices=["init", "update"])

plugins = {
        # "a":"url1",
        "ack":"https://github.com/mileszs/ack.vim.git",
        "airline":"https://github.com/vim-airline/vim-airline.git",
        "airline-themes":"https://github.com/vim-airline/vim-airline-themes.git",
        "auto-pairs":"https://github.com/jiangmiao/auto-pairs.git",
        "bookmarks":"https://github.com/MattesGroeger/vim-bookmarks.git",
        "ctrlp":"https://github.com/ctrlpvim/ctrlp.vim.git",
        "denite":"https://github.com/Shougo/denite.nvim.git",
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
        "unimpaired":"https://github.com/tpope/vim-unimpaired.git",
        "unite":"https://github.com/Shougo/unite.vim.git",
        "unite-gtags":"https://github.com/hewes/unite-gtags.git",
        "unite-outline":"https://github.com/Shougo/unite-outline.git",
        "unite-tag":"https://github.com/tsukkee/unite-tag.git",
        "vim-colors-solarized":"https://github.com/altercation/vim-colors-solarized.git",
        "vimwiki":"https://github.com/vimwiki/vimwiki.git",
        }


if __name__=="__main__":

    args = parser.parse_args()

    bundle = os.path.join(os.path.expanduser("~"), ".vim", "bundle")
    os.chdir(bundle)

    plugins = os.listdir()

    if args.what == "update":
        for p in plugins:

            print("* Updating {}".format(p))
            print(subprocess.check_output(
                ["git", "pull"],
                text=True,
                stderr=subprocess.STDOUT,
                cwd=os.path.join(bundle, p)))

    else:
        pass

        # for plug, url in plugins.iteritems():
            #os.system("echo {0} {1}".format(plug, url))
            # os.system("git clone --recursive {1} {0}".format(plug, url))

