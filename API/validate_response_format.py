import json
import requests


BASE_URL = "https://api.restful-api.dev"
#import os
#BASE_URL = os.getenv("BASE_URL")
def get_request():
    url = BASE_URL + "/objects?id=3&id=5"
    print(url)
    response = requests.get(url)
    json_data = response.json()
    json_str = json.dumps(json_data, indent=4)
    print("json response body: " + json_str)
    content_type = response.headers.get("Content-Type","").lower()
    print(content_type)
    assert "json" in content_type

get_request()