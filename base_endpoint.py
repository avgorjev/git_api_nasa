import os
import requests

API_KEY = os.environ['api_key']

print('my api_key is:', API_KEY)

url = f"https://api.nasa.gov/planetary/apod?api_key={API_KEY}"
payload = {}
headers = {}


print(requests.request("GET", url, headers=headers, data=payload).json())