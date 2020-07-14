import requests
import json
import jsonpath
import pytest


def test_Add_new_data():
    app_url = "http://thetestingworldapi.com/api/studentsDetails"
    f = open('/users/dmitry/Documents/Today/RequestJson.json', 'r')
    request_json = json.loads(f.read())
    response = requests.post(app_url, request_json)
    print(response.text)
    id = jsonpath.jsonpath(response.json(), 'id')
    print(id[0])

    tech_api_url = "http://thetestingworldapi.com/api/technicalskills"
    f = open('/users/dmitry/Documents/Today/TechDetail.json', 'r')
    request_json = json.loads(f.read())
    request_json['id'] = int(id[0])
    request_json['st_id'] = id[0]
    response = requests.post(tech_api_url, request_json)
    print(response.text)

    # address_api_url = "http://thetestingworldapi.com/api/addresses"
    # f = open('/users/dmitry/Documents/Today/addresses.json', 'r')
    # request_json = json.loads(f.read())
    # request_json['stId'] = id[0]
    # response = requests.post(address_api_url, request_json)


    final_details = "http://thetestingworldapi.com/api/FinalStudentDetails/"+str(id[0])
    response = requests.get(final_details)
    print(response.text)

