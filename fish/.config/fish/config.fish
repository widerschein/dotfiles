set -U fish_greeting

bind -M insert -m default jk repaint

# Colors
set -g fish_color_user yellow


# FZF
set -g FZF_DEFAULT_COMMAND 'rg --hidden --files'

# Autojump
if test -d ~/.autojump
    source ~/.autojump/share/autojump/autojump.fish
end


# Prompt
#set -g __fish_git_prompt_shorten_branch_len 10
#set -g __fish_git_prompt_describe_style describe
#set -g __fish_git_prompt_show_informative_status 1

# Aliases


