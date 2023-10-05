import requests
import json


def new_link():
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


def new_cus_link():
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


def new_full_link():
    url = "https://gotiny.cc/api"
    payload = json.dumps({
        "long": "https://amazon.com/very-long-url",
        "custom": "amazon",
        "useFallback": True
    })
    headers = {'Content-Type': 'application/json'}
    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text)


def link_as_text():
    url = "https://gotiny.cc/api/br7a3x"
    payload = {}
    headers = {}
    response = requests.get(url, headers=headers, data=payload)
    print(response.text)


def link_as_json():
    url = "https://gotiny.cc/api/nmytrk"
    payload = {}
    headers = {}
    response = requests.get(
        url,
        headers=headers,
        data=payload
    )
    new_data = json.loads(response)
    print(new_data)


print(new_link())
print(new_cus_link())
print(new_full_link())
print(link_as_text())
print(link_as_json())
