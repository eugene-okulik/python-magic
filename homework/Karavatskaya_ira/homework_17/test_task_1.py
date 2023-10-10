import requests
import pytest
import json


@pytest.fixture(scope="session", autouse=True)
def setup_and_teardown():
    print("Start testing")
    yield
    print("Testing completed")


@pytest.fixture(autouse=True)
def before_and_after_test():
    print("before test")
    yield
    print("after test")


@pytest.mark.parametrize("long_url", [
    "http://amazon.com/very-long-url",
    "http://example.com",
    "http://google.com"
])
def test_create_link(long_url):
    url = "https://gotiny.cc/api"
    payload = json.dumps({
        "long": long_url
    })
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, headers=headers, data=payload).json()
    assert response["status"] == 201


@pytest.mark.critical
def test_link_as_text():
    url = "https://gotiny.cc/api/br7a3x"
    payload = {}
    headers = {}
    response = requests.get(url, headers=headers, data=payload)
    assert response.status_code == 200


@pytest.mark.medium
def test_link_as_json():
    response = requests.get('https://gotiny.cc/api/nmytrk?format=json').json()
    assert "data" in response
