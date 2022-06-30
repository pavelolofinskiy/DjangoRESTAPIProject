import requests


endpoint = "https://httpbin.org/anything"

get_response = requests.get(endpoint, json={"query": "Hello world"})
print(get_response.text) # print raw text response

print(get_response.json())
print(get_response.status_code)
