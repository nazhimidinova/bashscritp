#!/bin/bash


function _create_usr  {
    read -p "Enter username: " username
    read -sp "Enter password: " password
    useradd $username -p $password -c "User created through scrypt"

    echo $(id $username | awk -F " " '{ print $1 }')
}


#user_uid=$(_create_usr)

#echo $user_uid