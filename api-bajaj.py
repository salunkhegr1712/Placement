#step 1
import requests
import base64

encoded = base64.b64encode('data to be encoded'.encode('ascii'))
print(encoded)

url = 'https://bfhldevapigw.healthrx.co.in/bfl-api-challenge/challenge-entry'
myobj = {
 "b_name": base64.b64encode("Yash sudhakar Jogdand".encode('ascii')).decode(),
 "name": "Yash sudhakar Jogdand",
 "b_reg_no": base64.b64encode("111907065".encode('ascii')).decode(),
 "reg_no": "111907065",
 "b_email": base64.b64encode("jogdandys19.extc@coep.ac.in".encode('ascii')).decode(),
 "email": "jogdandys19.extc@coep.ac.in"
}

x = requests.post(url, json = myobj)

print(x.text)
print(x.status_code)
# step 2
import base64
import requests


data = {
    "b_name": base64.b64encode("YASH_SUDHAKAR_JOGDAND".encode("ascii")).decode(),
    "name": "YASH_SUDHAKAR_JOGDAND",
    "b_reg_no": base64.b64encode("111907065".encode("ascii")).decode(),
    "reg_no": "111907065",
    "b_email": base64.b64encode("jogdandys19.extc@coep.ac.in".encode("ascii")).decode(),
    "email": "jogdandys19.extc@coep.ac.in",
#     //ENTER CODE YOU GET IN AFTER COMPLETING STEP ONE
    "personal_code": "KAFKA"
}

url = "https://bfhldevapigw.healthrx.co.in/bfl-api-challenge/challenge-final"
response = requests.post(url=url, json=data)

print(response.status_code)
print(response.content)
