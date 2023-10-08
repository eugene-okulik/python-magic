import requests
import json


def n_linc():
    body = json.dumps({
        "input": "http://amazon.com/very-long-url"
    })
    headers = {"Content-Type": "application/json"}
    response_1 = requests.post("https://gotiny.cc/api", headers=headers, data=body).json()
    print(response_1)


n_linc()


def new_custom_linc():
    url = "https://gotiny.cc/api"
    payload = json.dumps({
        "long": "https://amazon.com/very-long-url",
        "custom": "amazon"
    })
    headers = {'Content-Type': 'application/json'}
    response_2 = requests.post(url,headers=headers, data=payload).json()
    print(response_2)


new_custom_linc()


def new_full_link():
    url = "https://gotiny.cc/api"
    payload = json.dumps({
        "long": "https://amazon.com/very-long-url",
        "custom": "amazon",
        "useFallback": False
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
