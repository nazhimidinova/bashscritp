#!/bin/bash

echo "--- Script to create Linux users ---"
read -p "How many users do you want to create?: " user_ct

function _create_usr  {
    read -p "Enter username: " username
    read -sp "Enter password: " password
    useradd $username -p $password -c "User created through scrypt"
}

if [ $user_ct -gt 1 ]; then
    echo "Creating multi-users"
    for user in $(seq 1 $user_ct); do
        read -p "Enter username: " username
        read -sp "Enter password: " password
        useradd $username -p $password -c "User created through scrypt"
    done



elif [ $user_ct -eq 1 ]; then
    echo "Creating single user"
    read -p "Enter username: " username
    read -sp "Enter password: " password
    useradd $username -p $password -c "User created through scrypt"

else
    echo "Wrong input. Try again"
fi
