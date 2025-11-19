import json
import requests
from jsonschema.exceptions import ValidationError
from jsonschema.validators import validate

BASE_URL = "https://api.restful-api.dev"
#import os
#BASE_URL = os.getenv("BASE_URL")
def get_request():
    url = BASE_URL + "/objects?id=3&id=5"
    print(url)
    schema = {
         "type": "array",
         "properties": {
            "id": {"type": "string"},
            "name": {"type": "string"},
            "data": {
                "type": "object",
                "properties": {
                    "year": {"type": "integer"},
                    "price": {"type": "number"},
                    "CPU model": {
                        "type": "string"
                    },
                    "Hard disk size": {
                        "type": "string"
                    }
                },
            }
        },
        "required": ["id", "name", "data"]
    }
    response = requests.get(url)
    json_data = response.json()
    json_str = json.dumps(json_data,indent=4)
    print("json response body: "+json_str)
    print("STATUS CODE " ,response.status_code)
    assert response.status_code == 200
    try:
        validate(schema=schema,instance=json_data)
        print("Schema Validation passed")
        print(type(json_data))
        print(type(json_data[0]["data"]))
    except ValidationError as e:
        print(type(json_data))
        print(type(json_data[0]["data"]))
        print ("Schema Validation Failed: ",e.message)
get_request()