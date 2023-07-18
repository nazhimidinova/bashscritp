import json
import requests
import inquirer
import os


TOKEN = os.getenv('digital_token')

with open('install.sh', 'r') as f:
    user_data_contents = f.read()

def get_digitalocean_options():
    headers = {"Authorization": f"Bearer {TOKEN}"}


    image_response = requests.get("https://api.digitalocean.com/v2/images", headers=headers)
    image_data = image_response.json()
    image_choices = [image["slug"] for image in image_data["images"]]

   
    size_response = requests.get("https://api.digitalocean.com/v2/sizes", headers=headers)
    size_data = size_response.json()
    size_choices = [size["slug"] for size in size_data["sizes"]]

    
    region_response = requests.get("https://api.digitalocean.com/v2/regions", headers=headers)
    region_data = region_response.json()
    region_choices = [region["slug"] for region in region_data["regions"]]

  
    ssh_key_response = requests.get("https://api.digitalocean.com/v2/account/keys", headers=headers)
    ssh_key_data = ssh_key_response.json()
    ssh_key_choices = [ssh_key["id"] for ssh_key in ssh_key_data["ssh_keys"]]

    questions = [
        inquirer.List('image', message='Choose an image:', choices=image_choices),
        inquirer.List('size', message='Choose size:', choices=size_choices),
        inquirer.List('region', message='Choose a region:', choices=region_choices),
        inquirer.List('ssh_key', message='Choose an SSH key:', choices=ssh_key_choices),
    ]

    answers = inquirer.prompt(questions)
    return answers

def create_digitalocean_droplet(options):
    headers = {"Content-Type": "application/json", "Authorization": f"Bearer {TOKEN}"}
    url = "https://api.digitalocean.com/v2/droplets"

    name = input('Please create a name for your droplet: ')
    data = {
        "name": name,
        "region": options['region'],
        "size": options['size'],
        "image": options['image'],
        "ssh_keys": [options['ssh_key']],
        "user_data": user_data_contents
    }

    do_resp = requests.post(url, headers=headers, json=data)
    
    print(do_resp.status_code)
    print(do_resp.json())

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
