import requests
import os

TOKEN = os.getenv('digital_token')

headers = {"Content-Type": "application/json", "Authorization": f"Bearer {TOKEN}"}
url = "https://api.digitalocean.com/v2/droplets"

data = '''{
    "name": "Project2",
    "region": "nyc1",
    "size": "s-1vcpu-1gb",
    "image": "centos-stream-8-x64",
    "ssh_keys": ["38621754"],
    "user_data": "install.sh"
}'''

do_resp = requests.post(url, headers=headers, data=data)
print(do_resp.text)
