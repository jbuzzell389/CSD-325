import requests
import json

response1 = requests.get('https://api-server.dataquest.io/economic_data/countries')
print(response1.status_code)

# No formatting

data = json.loads(response1.json())
print(f"Total countries: {len(data)}")
print(f"First country: {data[0]['short_name']}")

# Formatting

params = {
    'filter_by': 'region=Sub-Saharan Africa',
    'limit': 5
}

response2 = requests.get(
    "https://api-server.dataquest.io/economic_data/countries",
    params=params
)
data = json.loads(response2.json())
print(f"Limited results: {len(data)}")
print(f"First country: {data[0]['short_name']}")
