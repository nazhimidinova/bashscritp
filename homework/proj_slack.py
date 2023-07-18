import requests, os, 
TOKEN = os.getenv('digital_token')

with open('install.sh', 'r') as f:
    user_data_contents = f.read()

headers = {"Content-Type": "application/json", "Authorization": f"Bearer {TOKEN}"}
url = "https://api.digitalocean.com/v2/droplets"

data = {
    "name": "Project",
    "region": "nyc1",
    "image": "centos-stream-8-x64",
    "size": "s-1vcpu-1gb",
    "ssh_keys": ["38863768"],
    "user_data": user_data_contents
}

do_resp = requests.post(url, headers=headers, json=data)

print(do_resp.status_code)
print(do_resp.json())



#Slack Api call
import requests

def send_slack_message(slack_url, message):
    payload = {
        "text": message
    }
    response = requests.post(slack_url, json=payload)
    if response.status_code == 200:
        print("Slack message sent successfully.")
    else:
        print(f"Failed to send Slack message. Status code: {response.status_code}")

def main():
    slack_url = "https://hooks.slack.com/services/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"
    message = "The DigitalOcean droplet and webpage have been created successfully by Aizhamal!"

    send_slack_message(slack_url, message)

if __name__ == "__main__":
    main()
