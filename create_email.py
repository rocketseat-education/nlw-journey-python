import requests

payload = {
    "requestor": "YourNameOrAppName",
    "version": "1.0"
}
response = requests.post('https://api.nodemailer.com/user', json=payload)
if response.status_code == 200:
    account = response.json()
    print(account)
else:
    raise Exception(f'Could not create Ethereal account: {response.text}')

