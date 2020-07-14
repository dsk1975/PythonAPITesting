import requests
import json
import jsonpath
import pytest

# API URL
url = 'https://reqres.in/api/users'

# a= 100
# @pytest.mark.skipif(a>10, reason="Condition is not satisfied")
@pytest.fixture(scope="module")
def start_execution():
    global file
    file = open('/users/dmitry/Documents/Today/CreateUser.json', 'r')

@pytest.mark.New
def test_create_new_user(start_execution):
    # file = open('/users/dmitry/Documents/Today/CreateUser.json', 'r')
    json_input = file.read()
    request_json = json.loads(json_input)
    # print(request_json)
    # Make POST request with JSON input body
    response = requests.post(url, request_json)
    # print(response.content)
    # Validation response code
    assert response.status_code == 201
    # Fetch header from response
    # print(response.headers.get('Content-Length'))
    # # Parse response to Json format
    # response_json = json.loads(response.text)
    # # Pick ID using jsonpath
    # id = jsonpath.jsonpath(response_json,'id')
    # print(id[0])

@pytest.mark.Other
def test_create_other_user(start_execution):
    # Read input Json file
    # file = open('/users/dmitry/Documents/Today/CreateUser.json', 'r')
    json_input = file.read()
    request_json = json.loads(json_input)
    # print(request_json)
    # Make POST request with JSON input body
    response = requests.post(url, request_json)
    # print(response.content)
    # Validation response code
    # assert response.status_code == 201
    # Fetch header from response
    # print(response.headers.get('Content-Length'))
    # Parse response to Json format
    response_json = json.loads(response.text)
    # Pick ID using jsonpath
    id = jsonpath.jsonpath(response_json,'id')
    print(id)