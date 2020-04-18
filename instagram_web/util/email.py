import os
from flask import request
import requests

def send_message():
    print('sending email')
    return requests.post(
        "https://api.mailgun.net/v3/"+os.environ.get("MAILGUN_DOMAIN")+"/messages",
        auth=("api", os.environ.get('MAILGUN_PRIVATE_API_KEY')),
        data={"from": "Excited User <elisakhor94@gmail.com>",
              "to": ["elisakhor94@gmail.com"],
              "subject": "testerrrr",
              "text": "TEST 123!",
              "html":"<h3>nextagram</h3>"})