import json

import requests

BASE_URL = "https://api.restful-api.dev"
import os
#BASE_URL = os.getenv("BASE_URL")
def get_request():
    url = BASE_URL + "/objects?id=3&id=5"
    print(url)
    response = requests.get(url)
    json_data = response.json()
    json_str = json.dumps(json_data,indent=4)
    print("json response body: "+json_str)
    print("STATUS CODE " ,response.status_code)
    try:
        print("In TRY")
        assert json_data[0]["id"] == 3
        assert json_data[0]["name"] == "Apple iPhone 12 Pro Max"
        #assert json_data[0]["data"]["color"] == "Black"
        print(json_data[0]["data"]["color"])
        color = json_data[0]["data"]["color"]
        assert color == "Black"
    except AssertionError as e:
        print("Data Error ")



get_request()