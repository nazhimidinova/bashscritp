import json
import requests, inquirer
import subprocess
import os

TOKEN = os.getenv('digital_token')

with open('install.sh', 'r') as f:
    user_data_contents = f.read()

def get_image_choices():
    command = ["doctl", "compute", "image", "list"]
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    stdout, stderr = process.communicate()

    print("stdout:", stdout)  # Debugging output
    print("stderr:", stderr)  # Debugging output

    if process.returncode == 0:
        images = json.loads(stdout)
        return [image["slug"] for image in images]
    else:
        print(f"Failed to get image choices. Error: {stderr}")
        return []


def get_size_choices():
    command = ["doctl", "compute", "size", "list"]
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    stdout, stderr = process.communicate()

    print("stdout:", stdout)  # Debugging output
    print("stderr:", stderr)  # Debugging output

    if process.returncode == 0:
        sizes = json.loads(stdout)
        return [size["slug"] for size in sizes]
    else:
        print(f"Failed to get size choices. Error: {stderr}")
        return []


def get_region_choices():
    command = ["doctl", "compute", "region", "list"]
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    stdout, stderr = process.communicate()

    print("stdout:", stdout)  # Debugging output
    print("stderr:", stderr)  # Debugging output

    if process.returncode == 0:
        regions = json.loads(stdout)
        return [region["slug"] for region in regions]
    else:
        print(f"Failed to get region choices. Error: {stderr}")
        return []


def get_digitalocean_options():
    image_choices = get_image_choices()
    size_choices = get_size_choices()
    region_choices = get_region_choices()

    questions = [
        inquirer.List('image', message='Choose an image:', choices=image_choices),
        inquirer.List('size', message='Choose size:', choices=size_choices),
        inquirer.List('region', message='Choose a region:', choices=region_choices),
        inquirer.List('ssh_key', message='Choose an SSH key:', choices=['38863768']),
    ]
    answers = inquirer.prompt(questions)
    return answers


def create_digitalocean_droplet(options):
    headers = {"Content-Type": "application/json", "Authorization": f"Bearer {os.getenv('TOKEN')}"}
    url = "https://api.digitalocean.com/v2/droplets"

    name = input('Please create a name for your droplet:')
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
