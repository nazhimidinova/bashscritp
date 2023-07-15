import requests, inquirer, json, pprint
pp = pprint.PrettyPrinter(indent=4)

url = "https://f4idu2pd8h.execute-api.us-east-1.amazonaws.com/v1/info"
headers = {
        "Content-Type": "application/json",
        "Access-Control-Allow-Headers": "Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token",
        "Access-Control-Allow-Origin*": "*"
}

resp = requests.get(url, headers=headers)
data = resp.json()['body']
instructors = json.loads(data)[0]['staff']
instructors_question = [
    inquirer.List('name', message="Choose an instructor", choices=[x['name'] for x in instructors])
]
user_resp = inquirer.prompt(instructors_question)
for inst in instructors:
    if inst['name'] == user_resp['name']:
        email = inst['email']
        print(f'''
******** Info for {inst['name']} **************
Name: {inst['name']}
Title: {inst['title']}
Email: {inst['email']}
''')


url = "https://f4idu2pd8h.execute-api.us-east-1.amazonaws.com/v1/email"
headers = {
        "Content-Type": "application/json",
        "Access-Control-Allow-Headers": "Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token",
        "Access-Control-Allow-Origin*": "*"
}
data1 = {"name": "Abdul Sharif", f'email': '{email}', "subject": "Localhost at your service", "message": "This message from not lambda but localhost"}
response = requests.post(url, headers=headers, json=data1)
print(response)