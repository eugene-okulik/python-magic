import json
import requests
import pytest


@pytest.fixture(scope="session", autouse=True)
def before_all_tests():
    print("Start testing")
    yield
    print("Testing completed")


@pytest.fixture(autouse=True)
def before_each_test():
    print("before")
    yield
    print("after test")


@pytest.mark.parametrize("url", [
    "http://example.com",
    "http://google.com",
    "http://stackoverflow.com"
])
@pytest.mark.critical
def test_n_linc(url):
    body = json.dumps({
        "input": "http://amazon.com/very-long-url"
    })
    headers = {"Content-Type": "application/json"}
    response_1 = requests.post("https://gotiny.cc/api", headers=headers, data=body).json()
    print(response_1)


@pytest.mark.medium
def test_new_custom_linc():
    url = "https://gotiny.cc/api"
    payload = json.dumps({
        "long": "https://amazon.com/very-long-url",
        "custom": "amazon"
    })
    headers = {'Content-Type': 'application/json'}
    response_2 = requests.post(url, headers=headers, data=payload).json()
    print(response_2)


def test_new_full_link():
    url = "https://gotiny.cc/api"
    payload = json.dumps({
        "long": "https://amazon.com/very-long-url",
        "custom": "amazon",
        "useFallback": False
    })
    headers = {'Content-Type': 'application/json'}
    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text)


def test_link_as_text():
    url = "https://gotiny.cc/api/br7a3x"
    payload = {}
    headers = {}
    response = requests.get(url, headers=headers, data=payload)
    print(response.text)


def test_link_as_json():
    response = requests.get('https://gotiny.cc/api/nmytrk?format=json').json()
    print(response)
