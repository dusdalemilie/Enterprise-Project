#!/usr/bin/env python3

import json, requests, re

from flask import Flask
app = Flask(__name__)
from datetime import datetime
@app.route("/", methods=['GET'])
def hello_world():
    now =datetime.now()
    return "<p>I GOT IT!</p>" "The time now is" +now.strftime("%m/%d/%Y %H:%M:%S") +data

#this runs my api data
api_url = "http://ipwho.is/8.8.4.4"
response = requests.get(api_url)
data = response.text
parse_json = json.loads(data)
print(parse_json)
json.loads(data)

app.run()