function fish_user_key_bindings
    if type -q fzf_key_bindings
        fzf_key_bindings
    end

    # Use vi mode with emacs key bindings in insert mode
    fish_default_key_bindings -M insert
    fish_vi_key_bindings --no-erase insert
end
