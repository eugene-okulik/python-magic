import requests


def post():
    body = {
        "input": "https://amazon.com/very-long-url",
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.post(
        'https://gotiny.cc/api',
        json=body,
        headers=headers
    )
    print(response.json())


post()


def post_options():
    body = {
        "long": "https://amazon.com/very-long-url",
        "custom": "amazon"
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.post(
        'https://gotiny.cc/api',
        json=body,
        headers=headers
    )
    print(response.json())


post_options()


def post_options_fall():
    body = {
        "long": "https://amazon.com/very-long-url",
        "custom": "test-amazon",
        "userFallback": "false"
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.post(
        'https://gotiny.cc/api',
        json=body,
        headers=headers
    )
    print(response.json())


post_options_fall()


def long_url():
    response = requests.get('https://gotiny.cc/api/amazon')
    print(response.text)


long_url()


def long_url():
    response = requests.get('https://gotiny.cc/api/amazon?format=json').json()
    print(response)


long_url()
