

import json
import jsonpath
import requests
import pytest

def test_add_new_student():
    global id
    url = "http://thetestingworldapi.com/api/studentsDetails"
    file = open("postJson",'r')
    request_json = json.loads(file.read())
    response = requests.post(url, request_json)
    response_json = response.json()
    id = jsonpath.jsonpath(response_json, 'id')
    print(id[0])


def test_getStudentDetails():
    finalURL = "http://thetestingworldapi.com/api/studentsDetails/" + str(id[0])
    response = requests.get(finalURL)
    print(response.text)