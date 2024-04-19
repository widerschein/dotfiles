# Remove greeter text
set -U fish_greeting

# Colors
set -g fish_color_user yellow

# fzf
set -g FZF_DEFAULT_COMMAND 'rg --hidden --files'

# Autojump
if test -d ~/.autojump
    source ~/.autojump/share/autojump/autojump.fish
end

# Bass
set -l bass_dir ~/Programme/bass
if not test -d $bass_dir
    echo "Setting up bass"
    mkdir -p $bass_dir
    git clone https://github.com/edc/bass.git $bass_dir
    make -C $bass_dir install
end
