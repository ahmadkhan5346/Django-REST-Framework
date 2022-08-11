import requests, json

URL = "http://127.0.0.1:8000/teacher/"

data = {
    'name':'Ali Abbas',
    'id_no':'104',
    'city':'Pune'
}

json_data = json.dumps(data)
r = requests.post(url = URL, data = json_data)
data = r.json()
print(data)