# @file
# content_api_example.py
#
# Bare-bones example showing how to use the Content API to retrieve latest publications.
#
# (c) 2026, Capital Economics Ltd.

import requests
import json

# Replace with your api-key
API_KEY = '<replace with your api key>'

BASE_URL = 'https://api.capitaleconomics.com/json'

params = {
    'api-key': API_KEY,
    'page[limit]': 10,  # return the 10 most recent (default is 50, max 100)
}

response = requests.get(f'{BASE_URL}/node/publication', params=params)
response.raise_for_status()

publications = response.json()
print(json.dumps(publications, indent=2))
