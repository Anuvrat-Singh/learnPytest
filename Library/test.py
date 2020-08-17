import requests
import json
import jsonpath
import openpyxl
from Library import Library

def test_addMultipleStudent():
    #set url and read request json file

    url = "http://thetestingworldapi.com/api/studentsDetails"
    f = open("../newStudent")
    json_request = json.loads(f.read())

    obj = Library.Common("../ddTesting.xlsx", "Sheet1")
    col = obj.fetch_Column_Count()
    row = obj.fetch_row_count()
    headers = obj.fetch_keyNames()

    for i in range(2,row+1):           #last record is skipped hence rows+1
        updated_json_req = obj.update_json_request_with_data(i, json_request, headers)
        response = requests.post(url, updated_json_req)
        print(response.status_code)
        print(response.text)