import requests

url = "https://jsonplaceholder.typicode.com/posts/1"

response = requests.get(url)

print(response.status_code)
print(response.json())
print(type(response.json()))

assert response.status_code == 222
assert response.json()['id'] == 1
print("API test passed")