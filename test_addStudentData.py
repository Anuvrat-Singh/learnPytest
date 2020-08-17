


import json
import jsonpath
import requests
import pytest

url = "http://thetestingworldapi.com/api/studentsDetails"

def test_makePostRequest():
    file = open("postJson",'r')
    inputJson = json.loads(file.read())
    response = requests.post(url,inputJson)
    print(response.text)
    print(response.status_code)
    print("--------------------------------------------------")


def test_makeGetRequest():
    url = "http://thetestingworldapi.com/api/studentsDetails/149797"
    response = requests.get(url)
    print(response.text)
    jsom_response = response.json()
    print(jsom_response)
    print("----------------------------->>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")



def test_makePutRequest():
    url = "http://thetestingworldapi.com/api/studentsDetails/149797"
    file = open("putJson",'r').read()
    response = requests.put(url, file)
    json_response = response.json()
    print(json_response)


def test_makeDeleteRequest():
    url = "http://thetestingworldapi.com/api/studentsDetails/149797"
    response = requests.delete(url)
    print(response.json())