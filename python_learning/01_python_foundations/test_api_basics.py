import requests

def test_get_post():
    url = "https://jsonplaceholder.typicode.com/posts/1"
    response = requests.get(url)
    assert response.status_code == 200
    response_data = response.json()
    assert response_data["id"] == 1
    assert response_data["userId"] == 1