import os
import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

AIRTABLE_TOKEN = os.getenv('AIRTABLE_TOKEN')
AIRTABLE_BASE_ID = os.getenv('AIRTABLE_BASE_ID')
AIRTABLE_TABLE_ID = os.getenv('AIRTABLE_TABLE_ID')

AIRTABLE_URL = f"https://api.airtable.com/v0/{AIRTABLE_BASE_ID}"

def get_golf_scores():
    """Add scores to the Airtable."""
    url = f"{AIRTABLE_URL}/{AIRTABLE_TABLE_ID}"
    print(url)
    headers = {
      'Authorization': f'Bearer {AIRTABLE_TOKEN}',
      #'Content-Type': 'application/json'
    }

    response = requests.request("GET", url, headers=headers)

    print(response)

def post():
    new_data = {
            "records": [
                {
                    "fields": {
                        "Name": "2021-09-22",
                        "Notes": "Test"
                    }
                },
                {
                    "fields": {
                        "Name": "2021-09-22",
                        "Notes": "Test2",
                    }
                }
            ]
        }
    url = f"{AIRTABLE_URL}/{AIRTABLE_TABLE_ID}"
    headers = {
      'Authorization': f'Bearer {AIRTABLE_TOKEN}',
      'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=json.dumps(new_data))

    print(response)


if __name__ == '__main__':
  post()