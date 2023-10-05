import requests
import json


def new_link():
    payload = json.dumps({
        "input": "https://amazon.com/very-long-url"
    })
    headers = {
        'Content-Type': 'application/json'
    }
    first_response = requests.post(
        "https://gotiny.cc/api",
        headers=headers,
        data=payload
    ).json()

    print(first_response)
    assert first_response['long'] == "https://amazon.com/very-long-url"


def new_cus_link():
    url = "https://gotiny.cc/api"
    payload = json.dumps({
        "long": "https://google.com/very-long-url",
        "custom": "google"
    })
    headers = {
        'Content-Type': 'application/json'
    }
    second_response = requests.post(
        url,
        headers=headers,
        data=payload
    ).json()
    print(second_response)

def new_full_link():
    url = "https://gotiny.cc/api"
    payload = json.dumps({
        "long": "https://amazon.com/very-long-url",
        "custom": "amazon",
        "useFallback": True
    })
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text)

print(new_link())
