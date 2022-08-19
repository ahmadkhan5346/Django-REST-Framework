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
        'name':'Suhail', 'mobile':9920374940, 'city':'Saki Naka'
    }

    json_data = json.dumps(data)
    response = requests.post(url = URL, data = json_data)
    data = response.json()
    print(data)
# post_data()


def update_data():            # Udate Data
    data = {
        'id': 9,
        'city': '3 no. khadi',
    }

    json_data = json.dumps(data)
    response = requests.put(url = URL, data = json_data)
    data = response.json()
    print(data)
# update_data()


def delete_data():            # Delete Data
    data = {'id': 10}

    json_data = json.dumps(data)
    response = requests.delete(url = URL, data = json_data)
    data = response.json()
    print(data)
# delete_data()