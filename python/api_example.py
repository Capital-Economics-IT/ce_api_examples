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
API_KEY = '<replace with your api key>'

# Sample data to query, these are valid series as at July 2024
# to test the response for no matching data replace the series ids with invalid ones, e.g. 'INVALID_SERIES_ID'
SAMPLE_SERIES_IDS = ['ADECO_CCPIYY', 'ADECO_CPIYY']

# Base API URL
BASE_URL = 'https://api.capitaleconomics.com/middletier/1.0'


class GetMetaData:
    URL = f'{BASE_URL}/metadata'

    def query(self) -> dict:
        """Basic query to get meta data"""
        try:
            # Query parameters, see main README for more details
            query = {
                'api_key': API_KEY,  # see above
                'skey': ','.join(SAMPLE_SERIES_IDS),
                'f_code': '',  # or specify a frequency, e.g. 'M' for monthly
                't_code': '',  # or specify a type, e.g. 'F' for forecast
                'vers': '1',  # version of the API, omit for latest
            }
            url = f'{self.URL}?{UrlParse.urlencode(query)}'

            # Diagnostics
            print(f'\n# Url - {url}\n')

            response = requests.get(url)
            return json.loads(response.content)
        except Exception as e:
            print(f'Error: {e}')


class GetData:
    URL = f'{BASE_URL}/data'

    def query(self) -> dict:
        """Basic query to get data"""
        try:
            # Query parameters, see main README for more details
            query = {
                'api_key': API_KEY,  # see above
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

            response = requests.get(url)
            return json.loads(response.content)
        except Exception as e:
            print(f'Error: {e}')


# Get metadata
metadata = GetMetaData().query()
print(metadata)

# Get data
data = GetData().query()
print(data)
