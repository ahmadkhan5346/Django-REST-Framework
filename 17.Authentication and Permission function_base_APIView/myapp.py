from email import header
import requests
import json


URL = "http://127.0.0.1:8000/student/"

def get_data(id = None):      # Read data   
    data = {}
    if id is not None:
        data = {'id':id}

    json_data = json.dumps(data)
    headers = {'Content-Type':'application/json'}
    r = requests.get(url = URL, headers=headers, data = json_data)
    data = r.json()
    print(data)
# get_data(1)


def post_data():             # Create data
    data = {
        'name': 'suhail',
        'roll': '103',
        'city': 'Ashok Nagar'
    }
    headers = {'content-type': 'application/json'}
    json_data = json.dumps(data)
    response = requests.post(url = URL, headers=headers, data = json_data)
    data = response.json()
    print(data)
# post_data()


def update_data():            # Udate Data
    data = {
        'id': 4,
        'name': 'Sadik',
        'city': 'Tilak Nagar'
    }

    headers = {'content-type': 'application/json'}
    
    json_data = json.dumps(data)
    response = requests.put(url = URL, headers=headers, data = json_data)
    data = response.json()
    print(data)
# update_data()


def delete_data():            # Delete Data
    data = {'id': 4}

    headers = {'content-type': 'application/json'}

    json_data = json.dumps(data)
    response = requests.delete(url = URL, headers=headers, data = json_data)
    data = response.json()
    print(data)
delete_data()