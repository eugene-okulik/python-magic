import requests
import pytest
import json


@pytest.fixture(scope='session')
def hello():
    print('Start testing')
    yield
    print('Testing completed')


@pytest.fixture()
def start():
    print('before test')
    yield
    print('after test')


@pytest.mark.critical
def test_new_cus_link(hello, start):
    url = "https://gotiny.cc/api"
    payload = json.dumps({
        "long": "https://yahoo.com/very-long-url",
        "custom": "google"
    })
    headers = {'Content-Type': 'application/json'}
    second_response = requests.post(
        url,
        headers=headers,
        data=payload
    ).json()
    print(second_response)


@pytest.mark.parametrize('body', [json.dumps({"input": "https://amazon.com/very-long-url"}),
                                  json.dumps({"input": "https://yandex.com/very-long-url"}),
                                  json.dumps({"input": "https://safari.com/very-long-url"})
                                  ])
def test_new_link(body, start):
    headers = {'Content-Type': 'application/json'}
    first_response = requests.post(
        "https://gotiny.cc/api",
        headers=headers,
        data=body
    ).json()

    print(first_response)


def test_new_full_link(start):
    url = "https://gotiny.cc/api"
    payload = json.dumps({
        "long": "https://ozon.com/very-long-url",
        "custom": "ozon",
        "useFallback": True
    })
    headers = {'Content-Type': 'application/json'}
    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text)


@pytest.mark.medium
def test_link_as_text(start):
    url = "https://gotiny.cc/api/br7a3x"
    payload = {}
    headers = {}
    response = requests.get(url, headers=headers, data=payload)
    print(response.text)


def test_link_as_json(hello, start):
    response = requests.get('https://gotiny.cc/api/nmytrk?format=json').json()
    print(response)
