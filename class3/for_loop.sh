#!/bin/bash

for user in $(cat /etc/passwd | awk -F ":" '{print $1}'); do
    mkdir /tmp/users/$user
    echo "$user folder created $(ls -la /tmp/users/$user)"
done