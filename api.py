import json

import requests

#base_url = "https://api.restful-api.dev"

def get_request():
    url = BASE_URL + "/objects?id=3&id=5"
    print(url)
    response = requests.get(url)
    json_data = response.json()
    json_str = json.dumps(json_data,indent=4)
    print("json response body: "+json_str)

#get_request()

def post_request():
    url = base_url + "/objects"
    print(url)
    data = {
        "name": "Apple MacBook Pro 16",
        "data": {
            "year": 2019,
            "price": 1849.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB"
        }
    }
    response=requests.post(url,json=data)
    assert response.status_code == 200
    json_data = response.json();
    json_str = json.dumps(json_data,indent=4)
    print("PUT response: "+json_str)
    user_id = json_data["id"]
    assert "name" in json_data
    assert json_data["name"] == "Apple MacBook Pro 16"
    return user_id

user_id = post_request()

def put_request(user_id):
    url = base_url + f"/objects/{user_id}"
    data = {
    "name": "Apple MacBook Pro 20",
    "data": {
        "year": 2020,
        "price": 1849.99,
        "CPU model": "Intel Core i9",
        "Hard disk size": "1 TB"
        }
    }
    response = requests.put(url,json=data)
    assert response.status_code == 200
    json_data = response.json()
    json_str = json.dumps(json_data,indent=4)
    print("PUT response "+json_str)
    assert json_data["data"]["year"] == 2020
    print(json_data["data"]["year"])

put_request(user_id)

def delete_request(user_id):
    url = base_url + f"/objects/{user_id}"
    response = requests.delete(url)
    assert response.status_code == 200
    json_data = response.json()
    print (json_data["message"])

delete_request(user_id)