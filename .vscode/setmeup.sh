#!/bin/bash

## Quick Refs
##? To soft-reset (revert back) last git commit:
##^ git reset --soft HEAD~1
##? For soft-resetting last 3 git commits:
##^ git reset --soft HEAD~3

## Git Commands as Aliases
alias getrepo="git rev-parse --show-toplevel"
alias getrepo-dirname="basename $(getrepo)"
alias getrepo-dirpath="echo $(getrepo)"
alias getrepo-parentdir="dirname $(getrepo)"
alias getrepo-remote="git remote get-url origin"

# getrepo-remote | cut -d ":" -f2 | cut -d "." -f1

## Setconda Commands
alias setconda='. $(getrepo || pwd)/.vscode/setconda.sh'
alias baseconda='conda activate base'
#alias xmake="make -C $(getrepo || pwd)/.vscode"
alias xmake="make -f $(getrepo || pwd)/.vscode/Makefile"
alias setmeup='. $(getrepo || pwd)/.vscode/setmeup.sh'
