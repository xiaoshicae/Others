import json
import requests

url = 'http://127.0.0.1:5000/phone/register/verify/'

data = {
    "serialNum": 'reg123',
    "phone": '13568838680'
}

r = requests.post(url, data=json.dumps(data))
print(r.content.decode())


