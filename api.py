#!/usr/bin/env python3

from flask import Flask
app = Flask(__name__)
@app.route("/", methods=['GET'])
def hello_world():
    return "<p>I GOT IT!</p>" +data

from flask_restful import Api, Resource, reqparse
import random
import json, requests, re

#this runs my api data
api_url = "http://ipwho.is/8.8.4.4"
response = requests.get(api_url)
data = response.text
parse_json = json.loads(data)
print(parse_json)
json.loads(data)

app.run()