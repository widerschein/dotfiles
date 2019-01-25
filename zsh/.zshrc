autoload -U colors zsh/terminfo
autoload -Uz compinit

colors
compinit

eval "$(dircolors -b)"

#------------------------------------
# Completion
#------------------------------------

#zstyle ':completion:*::::' completer _expand _complete _ignored _approximate
zstyle ':completion:*' completer _complete _match _approximate
zstyle ':completion:*:match:*' original only
zstyle ':completion:*:approximate:*' max-errors 1 numeric

zstyle ':completion:*' menu select=1 _complete _ignored _approximate
zstyle ':completion:*' verbose yes

zstyle ':completion:*:descriptions' format ' %F{yellow}-- %d --%f'

zstyle ':completion:*' list-colors ${(s.:.)LS_COLORS}
zstyle ':completion:*' group-name ''
zstyle ':completion:*' format '%F{yellow}%d%f'
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
alias ll='ls -hal'
alias ..='cd ..'
alias ...='cd ../..'

alias pac='sudo pacman'
alias r='ranger'
alias nv='nvim'

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
