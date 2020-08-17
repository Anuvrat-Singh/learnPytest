import json
import requests
import jsonpath

def test_oAuthSample():
    token_url = "http://thetestingworldapi.com/Token"
    data = {'grant_type': 'password', 'username': 'admin', 'password'
    response = requests.post(token_url, data)
    print(response.text)
    print(response.status_code)
    # tokenValue = jsonpath.jsonpath(response.json(),'access_token')
    # url = "http://thetestingworldapi.com/api/StDetails/149851"
    # response = requests.get(url)
    # print(response.text)
