#!/bin/bash

if [ -d ".git" ]; then
    git status 
    git add $1
    git commit -m "$2"
    git push
fi