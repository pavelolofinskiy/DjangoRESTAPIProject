import requests


endpoint = "http://localhost:8000/api/"

get_response = requests.post(endpoint, json={"title": "123abc", "content": 'Hello world', 'price': 'abc123'})
#print(get_response.headers)
#print(get_response.text)
print(get_response.json())
