#!/bin/bash

echo "Starting the user data" > /root/text.txt
sudo yum update rpm -y
sudo yum install httpd zip -y
sudo systemctl start httpd

echo "Finishing installing packages" >> /root/text/txt

curl -O https://www.free-css.com/assets/files/free-css-templates/download/page293/photosec.zip
unzip photosec.zip
rm -rf photosec.zip

echo "Downloaded Website files" >> /root/text.txt

for file in $(ls); do 
    if [ $file = *"photosec"* ]; then
        cp -R $file/* /var/www/html/
    fi
done 

echo "Moved files to /var/www/html" >> /root/text.txt
