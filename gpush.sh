#!/bin/bash

if [ -d ".git" ]; then
    git status 
    git add $1
    git commit -m "$2"
    git push
    else
    echo " You arent in a repo"
    read -p "Enter your repo name: " repo
    repo_p=$(find ~/ -name scripting1 -type d)

    if [ $repo_p != -z ]; then 
        cd $repo_p 
        ls -la
    else  
        echo " repo $repo does not exist" 
    fi 
fi 