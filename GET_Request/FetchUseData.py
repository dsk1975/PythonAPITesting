
import requests
import json
import jsonpath


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
print(response.headers.get('Date', 'Server'))
# Feych value using Jsonpath
pages = jsonpath.jsonpath(json_response, 'data[0]')

# for val in json_response['data']:

    # print(val['id'])


# print(json_response)

print(pages[0])



# Fetch response header
# print(response.headers)
# Fetch specific header content
# print(response.headers.get('Date'))
# print(response.headers.get('Server'))

# Fetch cookies from header
# print(response.cookies)

# Fetch encoding
# print(response.encoding)
# # Fetch elapsed time
# print(response.elapsed)

# print(response.status_code)
# assert response.status_code == 200
