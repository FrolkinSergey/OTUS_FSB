import requests


def test_url_status(base_url: str, status_code: int):
    response = requests.get(base_url)
    assert response.status_code == status_code
