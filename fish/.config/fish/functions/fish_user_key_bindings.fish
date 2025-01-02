function fish_user_key_bindings
    #fzf --fish | source

    # Use vi mode with emacs key bindings in insert mode
    fish_default_key_bindings -M insert
    fish_vi_key_bindings --no-erase insert

    # Enter normal mode
    bind -M insert -m default jk repaint
end
