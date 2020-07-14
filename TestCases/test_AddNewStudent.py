import requests
import json
import jsonpath
import pytest


def test_add_student_data():
    API_URL = "http://thetestingworldapi.com/api/studentsDetails"
    f = open('/users/dmitry/Documents/Today/RequestJson.json', 'r')
    json_request = json.loads(f.read())
    response = requests.post(API_URL, json_request)
    print(response.text)


def test_update_student_data():
    API_URL = "http://thetestingworldapi.com/api/studentsDetails/52609"
    f = open('/users/dmitry/Documents/Today/RequestJson.json', 'r')
    json_request = json.loads(f.read())
    response = requests.put(API_URL, json_request)
    print(response.text)


def test_delete_student():
    API_URL = "http://thetestingworldapi.com/api/studentsDetails/52609"
    response = requests.delete(API_URL)
    print(response.text)


def test_get_student_data():
    API_URL = "http://thetestingworldapi.com/api/studentsDetails/52609"
    response = requests.get(API_URL)
    json_response = response.json()
    print(json_response)
    id = jsonpath.jsonpath(json_response, 'data.id')
    assert id[0] == 52609