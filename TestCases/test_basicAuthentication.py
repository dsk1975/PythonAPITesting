import requests
from requests.auth import HTTPBasicAuth

def test_with_authentication():
    response = requests.get('https://api.github.com/user', auth= HTTPBasicAuth('dsk1975','h887A4Q2$7'))
    print(response.text)
test_with_authentication()