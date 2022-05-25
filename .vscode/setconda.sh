#!/bin/bash

### File: setconda.sh

# To run this script from project root directory:
# RUN: . .vscode/setconda.sh

# SETMEUP_GIST_URL="https://gist.githubusercontent.com/sugatoray/64e6c4c4ab42ef42a76be4a658712c4d/raw/b37a70aea4d782d1a61b8129ce185844ec4691e0/setmeup.sh"
# cd .vscode && curl $SETMEUP_GIST_URL -o setmeup.sh && cd ..

alias getrepo="git rev-parse --show-toplevel"
alias getrepo-dirname="basename $(getrepo)"
alias getrepo-dirpath="echo $(getrepo)"
alias getrepo-parentdir="dirname $(getrepo)"
alias getrepo-remote="git remote get-url origin"
# getrepo-remote | cut -d ":" -f2 | cut -d "." -f1

alias setconda='. $(getrepo || pwd)/.vscode/setconda.sh'
alias baseconda='conda activate base'
#alias xmake="make -C $(getrepo || pwd)/.vscode"
alias xmake="make -f $(getrepo || pwd)/.vscode/Makefile"
alias setmeup='. $(getrepo || pwd)/.vscode/setmeup.sh'

PROJECT_NAME="systemsetup"
PROJECT_CONDA_ENV="pytorch_env"

PROJECT_NAME="$(getrepo-dirname || echo $PROJECT_NAME)"

formatsetconda $PROJECT_NAME $PROJECT_CONDA_ENV

unset \
    PROJECT_NAME \
    PROJECT_CONDA_ENV
