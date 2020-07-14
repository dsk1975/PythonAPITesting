
import requests
import json
import jsonpath


# API URL

url = 'https://reqres.in/api/users/2'

# Read input Json file
file = open('/users/dmitry/Documents/Today/CreateUser.json', 'r')

json_input = file.read()
request_json = json.loads(json_input)

# print(request_json)

# Make PUT request with JSON input body

response = requests.patch(url, request_json)
print(response.content)

# Validation response code
assert response.status_code == 200

# Fetch header from response


# print(response.headers.get('Content-Length'))

# Parse response to Json format

response_json = json.loads(response.text)

 # Pick ID using jsonpath
update = jsonpath.jsonpath(response_json,'updatedAt')
#
print(update[0])