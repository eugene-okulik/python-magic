import requests
import json


def new_link():
    body = json.dumps({
        "input": "https://amazon.com/very-long-url"
    })
    headers = {'Content-Type': 'application/json'}
    response = requests.post("https://gotiny.cc/api", headers=headers, data=body).json()
    print(response)


new_link()


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


new_cus_link()


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


new_full_link()


def link_as_text():
    url = "https://gotiny.cc/api/br7a3x"
    payload = {}
    headers = {}
    response = requests.get(url, headers=headers, data=payload)
    print(response.text)


link_as_text()


def link_as_json():
    response = requests.get('https://gotiny.cc/api/nmytrk?format=json').json()
    print(response)


link_as_json()
