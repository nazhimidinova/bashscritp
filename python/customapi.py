import requests, pprint, json, inquirer
pp = pprint.PrettyPrinter(indent=4)
url = "https://f4idu2pd8h.execute-api.us-east-1.amazonaws.com/v1/info"
headers = {
        "Content-Type": "application/json",
        "Access-Control-Allow-Headers": "Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token",
        "Access-Control-Allow-Origin*": "*"
}

resp = requests.get(url, headers=headers)
data = resp.json()['body']
info = json.loads(data)
sessions = info[1]
session_choices = [
    inquirer.List('session', message="Choose a session", choices=[x['name'] for x in sessions['sessions']])
]
user_select = inquirer.prompt(session_choices)


for x in sessions['sessions']:
    if x['name'] == user_select['session']:
        print(f"""
********* Info for {user_select['session']} *********

- Duration: {x['duration']}
- Prerequisets: {x['prerequisets']}
- Certificates: {x['certificates']}
- Instructor: {x['instructor']}
- Price: {x['price']}
        """)



#for staff in info[0]['staff']:
    #if staff['name'] == 'Abdul Sharif':
        #print(f"Abdul is currently {staff['title']}")
    