# @file
# content_api_example.py
#
# Bare-bones example showing how to use the Content API to retrieve latest publications.
#
# (c) 2026, Capital Economics Ltd.

import requests
import json
from datetime import datetime

# Replace with your api-key
API_KEY = '<replace with your api key>'

BASE_URL = 'https://api.capitaleconomics.com/json'

# Data returned is automatically filtered to items matching your subscription,
# but can be filtered down further by specifying specific service tags.
service_tags = [
    'Commodities',
    'Middle East Rapid Response',
]

params = {
    'api-key': API_KEY,
    # Example limit the number of items returned...
    'page[limit]': 1,
    # Example date filtering...
    'filter[published_at][condition][path]': 'published_at',
    'filter[published_at][condition][operator]': '>=',
    'filter[published_at][condition][value]': int(datetime.fromisoformat('2026-01-01T00:00:00+00:00').timestamp()),
    # Example filtering by specific service tags...
    'filter[service_names][condition][path]': 'field_service.name',
    'filter[service_names][condition][operator]': 'IN',
    'filter[service_names][condition][value][]': service_tags
}

response = requests.get(f'{BASE_URL}/node/publication', params=params)
response.raise_for_status()

publications = response.json()
print(json.dumps(publications, indent=2))
