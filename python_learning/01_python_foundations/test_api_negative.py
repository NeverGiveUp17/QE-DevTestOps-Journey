import requests

def test_get_non_existing_post():
    url = "https://jsonplaceholder.typicode.com/posts/9999"
    response = requests.get(url)
    assert response.status_code == 404
    response_data = response.json()
    assert response_data == {}