import json
import jsonpath
import requests
import pytest

def test_add_new_student():
    url = "http://thetestingworldapi.com/api/studentsDetails"
    file = open("postJson",'r')
    request_json = json.loads(file.read())
    response = requests.post(url, request_json)
    response_json = response.json()
    id = jsonpath.jsonpath(response_json, 'id')
    print(id[0])

    url = "http://thetestingworldapi.com/api/technicalskills"
    file = open("techDetails",'r')
    request_json = json.loads(file.read())
    request_json['id'] = int(id[0])
    request_json['st_id'] = int(id[0])
    response = requests.post(url,request_json)
    print(response.text)

    addressURL = "http://thetestingworldapi.com/api/addresses"
    file = open("addressJson",'r')
    request_json = json.loads(file.read())
    request_json['stId'] = int(id[0])
    response = requests.post(addressURL,request_json)
    print(response.json())

    finalURL = "http://thetestingworldapi.com/api/studentsDetails/" + str(id[0])
    response = requests.get(finalURL)
    print(response.json())

