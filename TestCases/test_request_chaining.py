import requests
import jsonpath
import json
import pytest

def test_add_new_student():
    global id
    api_url = "http://thetestingworldapi.com/api/studentsDetails"
    f =open('/users/dmitry/Documents/Today/AddStudent.json', 'r')
    json_request = json.loads(f.read())
    response = requests.post(api_url, json_request )
    id = jsonpath.jsonpath(response.json(),'id')
    print(id[0])

def test_get_details():
    api_url = "http://thetestingworldapi.com/api/studentsDetails/"+str(id[0])
    response = requests.get(api_url)
    print(response.text)