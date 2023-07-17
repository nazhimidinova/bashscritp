import requests
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

def create_digitalocean_droplet(options):
    TOKEN = os.getenv('digital_token')
    headers = {"Content-Type": "application/json", "Authorization": f"Bearer {TOKEN}"}
    url = "https://api.digitalocean.com/v2/droplets"

    template_url = "https://github.com/pro-dev-ph/bootstrap-simple-admin-template/blob/main/template.html"  # Replace this URL with the actual template URL

    # Download the HTML template
    html_save_path = "/var/www/html/template.html"
    download_template(template_url, html_save_path)

    user_data = f'''
#!/bin/bash
apt-get update
apt-get -y install apache2
echo "<link rel='stylesheet' type='text/css' href='/template.css'>" >> /var/www/html/index.html
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
