

import requests
from requests.auth import HTTPBasicAuth

def test_basicAuth():
    url = "https://api.github.com/user"
    response = requests.get(url,auth=HTTPBasicAuth('anuvrat-singh',''))
    print(response.text)
    print(response.status_code)