#!/bin/bash
# Count dns name server in the /etc/resolv.conf if found
for file in /etc/*
do
        # check if file exists in bash using the if #  
    if [ "${file}" == "/etc/resolv.conf" ]
    then
        countNameservers=$(grep -c nameserver /etc/resolv.conf)
        echo "Total dns ${countNameservers} nameservers defined in ${file}"
        break
    fi
done