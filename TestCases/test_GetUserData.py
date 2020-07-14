import requests
import json
import jsonpath
import pytest

@pytest.mark.Det
def test_Fetch_user_details():
    # API URL
    url = 'https://reqres.in/api/users?page=2'
    # Sent Get requests
    response = requests.get(url)
    # print(response)
    # Display response content
    # print(response.content)
    # Parse response to Json format
    json_response = json.loads(response.text)
    # print(json_response)
    # print(response.headers.get('Date', 'Server'))
    # Feych value using Jsonpath
    for i in range(0, 3):
        first_name = jsonpath.jsonpath(json_response, 'data[+str(i)+].first_mame')
        print(first_name)


