import requests


endpoint = "http://localhost:8000/api/products/1/update/"

data = {
    'title': "Hello world my old droog",
    'price': 123.22
}

get_response = requests.put(endpoint, json=data)
print(get_response.json())
