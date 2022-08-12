import requests
import json


URL = "http://127.0.0.1:8000/contactapi/"

def get_data(id = None):      # Read data   
    data = {}
    if id is not None:
        data = {'id':id}

    json_data = json.dumps(data)
    r = requests.get(url = URL, data = json_data)
    data = r.json()
    print(data)

# get_data()

def post_data():             # Create data
    data = {
        'name':'Ashraf', 'mobile':9004542268, 'city':'Mankhurd'
    }

    json_data = json.dumps(data)
    response = requests.post(url = URL, data = json_data)
    data = response.json()
    print(data)

# post_data()