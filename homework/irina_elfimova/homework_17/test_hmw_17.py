import requests
import json


def test_new_link():
    body = json.dumps({
        "input": "https://amazon.com/very-long-url"
    })
    headers = {'Content-Type': 'application/json'}
    first_response = requests.post(
        "https://gotiny.cc/api",
        headers=headers,
        data=body
    ).json()

    print(first_response)


def test_new_cus_link():
    url = "https://gotiny.cc/api"
    payload = json.dumps({
        "long": "https://google.com/very-long-url",
        "custom": "google"
    })
    headers = {'Content-Type': 'application/json'}
    second_response = requests.post(
        url,
        headers=headers,
        data=payload
    ).json()
    print(second_response)


def test_new_full_link():
    url = "https://gotiny.cc/api"
    payload = json.dumps({
        "long": "https://amazon.com/very-long-url",
        "custom": "amazon",
        "useFallback": True
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
