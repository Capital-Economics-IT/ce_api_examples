# @file
# api_example.py
#
# Bare-bones API example showing how to use the API to get both metadata & data.
#
# (c) 2024, Capital Economics Ltd.

import requests
from requests.auth import HTTPBasicAuth

import json
import urllib.parse as UrlParse

# Replace with your username & password
USERNAME = '<replace with your credentials>'
PASSWORD = '<replace with your credentials>'

# Sample data to query
SAMPLE_SERIES_IDS = ['ADECO_CCPIYY', 'ADECO_CPIYY']

# Base API URL
BASE_URL = 'https://capitaleconomics.com/api/middletier'


class GetMetaData:
    URL = f'{BASE_URL}/metadata/prod'

    def query(self) -> dict:
        """Basic query to get meta data"""
        try:
            # Query parameters, see main README for more details
            query = {
                'skey': ','.join(SAMPLE_SERIES_IDS),
                'f_code': '',  # or specify a frequency, e.g. 'M' for monthly
                't_code': '',  # or specify a type, e.g. 'F' for forecast
                'vers': '1',  # version of the API, omit for latest
            }
            url = f'{self.URL}?{UrlParse.urlencode(query)}'

            # Diagnostics
            print(f'\n# Url - {url}\n')

            response = requests.get(url, auth=HTTPBasicAuth(USERNAME, PASSWORD))
            return json.loads(response.content)
        except Exception as e:
            print(f'Error: {e}')


class GetData:
    URL = f'{BASE_URL}/data/prod'

    def query(self) -> dict:
        """Basic query to get data"""
        try:
            # Query parameters, see main README for more details
            query = {
                'skey': ','.join(SAMPLE_SERIES_IDS),
                'f_code': 'M',  # Monthly, other frequencies Y/Q/M/W/D
                't_code': '',  # or specify a type, e.g. 'F' for forecast
                'start_date': '2020-01-01',  # start of 2020
                'end_date': '2021-12-31',  # end of 2021
                'series_info': 'true',
                'vers': '1',  # version of the API, omit for latest
            }
            url = f'{self.URL}?{UrlParse.urlencode(query)}'

            # Diagnostics
            print(f'\n# Url - {url}\n')

            response = requests.get(url, auth=HTTPBasicAuth(USERNAME, PASSWORD))
            return json.loads(response.content)
        except Exception as e:
            print(f'Error: {e}')


# Get metadata
metadata = GetMetaData().query()
print(metadata)

# Get data
data = GetData().query()
print(data)
