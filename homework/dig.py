import requests
import inquirer
import os

def download_template(template_url, save_path):
    try:
        response = requests.get(template_url)
        if response.status_code == 200:
            with open(save_path, 'w', encoding='utf-8') as file:
                file.write(response.text)
            return True
        else:
            print(f"Failed to download the template. Status code: {response.status_code}")
            return False
    except requests.exceptions.RequestException as e:
        print(f"Error downloading the template: {e}")
        return False

def get_digitalocean_options():
    questions = [
        inquirer.List('image', message='Choose an image:', choices=['ubuntu-20-04-x64', 'centos-8-x64']),
        inquirer.List('size', message='Choose a size:', choices=['s-1vcpu-1gb', 's-2vcpu-2gb']),
        inquirer.List('region', message='Choose a region:', choices=['nyc1', 'sfo2']),
        inquirer.List('ssh_key', message='Choose an SSH key:', choices=['38863768']),
    ]
    answers = inquirer.prompt(questions)
    return answers

def create_digitalocean_droplet(options):
    TOKEN = os.getenv('digital_token')
    headers = {"Content-Type": "application/json", "Authorization": f"Bearer {TOKEN}"}
    url = "https://api.digitalocean.com/v2/droplets"

    template_url = "https://github.com/pro-dev-ph/bootstrap-simple-admin-template/blob/main/404.html"
    css_url = "https://github.com/pro-dev-ph/bootstrap-simple-admin-template/raw/main/template.css"

    # Update the save paths to a local directory where you have write permissions
    html_save_path = "./template.html"
    css_save_path = "./template.css"

    download_template(template_url, html_save_path)
    download_template(css_url, css_save_path)

    user_data = f'''
#!/bin/bash
apt-get update
apt-get -y install apache2
echo "<link rel='stylesheet' type='text/css' href='/template.css'>" >> /var/www/html/template.html
systemctl start apache2
'''

    data = {
        "name": "Project2",
        "region": options['region'],
        "size": options['size'],
        "image": options['image'],
        "ssh_keys": [options['ssh_key']],
        "user_data": user_data
    }

    do_resp = requests.post(url, headers=headers, json=data)
    return do_resp

def main():
    options = get_digitalocean_options()
    response = create_digitalocean_droplet(options)
    
    if response.status_code == 202:
        print("Droplet created successfully.")
    else:
        print("Droplet creation failed.")

if __name__ == "__main__":
    main()
