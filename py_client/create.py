import requests


headers = {'Authorization': 'Bearer ac7beabe9347e2ab7f638ec3c0bcbfeeaa05ef92'}

endpoint = "http://localhost:8000/api/products/"

data = {
    'title': 'This field is done',
    'price': 32.99
}

get_response = requests.post(endpoint, json=data, headers=headers)
print(get_response.json())
