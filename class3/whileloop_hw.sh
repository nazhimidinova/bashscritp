#!/bin/bash

file=aika.txt

while read -r line;
do 
    echo $line
done < "$file"
