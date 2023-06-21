#!/bin/bash

sudo yum update rpm -y 
sudo yum update -y 

sudo yum install git -y 

git config --global user.name "nazhimidinova"
git config --global user.email "aika.nazhimidinova@gmail.com" 

git clone https://github.com/nazhimidinova/bashscritp.git /root/bashscript
