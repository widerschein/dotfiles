if [ -f ~/.dynardorc ]; then
    . ~/.dynardorc 
fi

#export PATH=$PATH:$HOME/.local/bin:$HOME/bin_dev

export EDITOR=nvim

# autojump
[[ -s ~/.autojump/etc/profile.d/autojump.sh ]] && source ~/.autojump/etc/profile.d/autojump.sh

# completions
#fpath=(~/Programme/zsh-completions/src $fpath)

setxkbmap -option ctrl:nocaps


autoload -U colors zsh/terminfo
autoload -Uz compinit

colors
compinit

eval "$(dircolors -b)"

#------------------------------------
# Completion
#------------------------------------


zstyle ':completion:*::::' completer _expand _complete _ignored _approximate
zstyle ':completion:*' menu select=1 _complete _ignored _approximate
zstyle ':completion:*' verbose yes

zstyle ':completion:*:descriptions' format ' %F{yellow}-- %d --%f'

zstyle ':completion:*' list-colors ${(s.:.)LS_COLORS}
zstyle ':completion:*' group-name ''
zstyle ':completion:*' format '%F{yellow}%d%f'
zstyle ':completion:*' max-errors 1 numeric
zstyle ':completion:*' original false
zstyle ':completion:*' matcher-list 'm:{a-z}={A-Z}'
#zstyle ':completion:*' select-prompt %SScrolling active: current selection at %p%s
zstyle :compinstall filename '/home/sharkus/.zshrc'



# Directories
#zstyle ':completion:*:default' list-colors ${(s.:.)LS_COLORS}
zstyle ':completion:*:*:cd:*' tag-order local-directories directory-stack path-directories
zstyle ':completion:*:*:cd:*:directory-stack' menu yes select

# Kill
zstyle ':completion:*:*:*:*:processes' command 'ps -u $LOGNAME -o pid,user,command -w'
zstyle ':completion:*:*:kill:*:processes' list-colors '=(#b) #([0-9]#) ([0-9a-z-]#)*=01;36=0=01'
zstyle ':completion:*:*:kill:*' menu yes select
zstyle ':completion:*:*:kill:*' force-list always
zstyle ':completion:*:*:kill:*' insert-ids single

# gdb attach
zstyle ':completion:*:*:gdb:*' command 'ps -u $LOGNAME -o pid,user,command -w'


setopt COMPLETE_IN_WORD
setopt AUTO_MENU           # Show completion menu on a successive tab press.
setopt AUTO_LIST           # Automatically list choices on ambiguous completion.

#------------------------------------
# Aliases
#------------------------------------

alias ls='ls --color'
alias ll='ls -l'
alias ..='cd ..'
alias ...='cd ../..'

alias nv='nvim'
alias r='ranger'
alias f='fzf'

alias gs='git status'
alias ga='git add'
alias gb='git branch'
alias gc='git commit'
alias gps='git push'
alias gpl='git pull -r'
alias stash='git stash'
alias pop='git stash pop'

#------------------------------------
# Prompt
#------------------------------------


autoload -Uz vcs_info
zstyle ':vcs_info:*' enable git hg
zstyle ':vcs_info:*' check-for-changes true

precmd () {
    vcs_info
}

setprompt() {
  setopt prompt_subst

  if [[ -n "$SSH_CLIENT"  ||  -n "$SSH2_CLIENT" ]]; then
    p_host='%F{yellow}%M%f'
  else
    p_host='%F{green}%M%f'
  fi

  PROMPT='%(!.%F{red}%n%f.%F{yellow}%n%f)%F{cyan}@%f%F{red}${p_host}%f %F{blue}%C%f%  '

  #RPROMPT=$'${vcs_info_msg_0_}'
}
setprompt


#------------------------------------
# History
#------------------------------------
HISTFILE=~/.histfile
HISTSIZE=9000
SAVEHIST=9000

setopt append_history
setopt hist_ignore_dups

#------------------------------------
# Configuration
#------------------------------------

bindkey -e
#unsetopt menu_complete

bindkey "^[[1~" beginning-of-line
bindkey "^[[4~" end-of-line
bindkey "^[[3~" delete-char

