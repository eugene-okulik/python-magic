import requests


def new_link(long_link):
    body = {
        "input": f"{long_link}"
    }
    headers = {"Content-Type": "application/json"}
    response = requests.post(
        'https://gotiny.cc/api',
        json=body,
        headers=headers
    )
    return response.json()['code']


def get_link(code):
    response = requests.get(f'https://gotiny.cc/api/{code}')
    return response.text


def creat_simple_link():
    long_link = 'https://hh.ru/search/vacancyitems_on_page=50'
    body = {
        "input": long_link
    }
    headers = {"Content-Type": "application/json"}
    response = requests.post(
        'https://gotiny.cc/api',
        json=body,
        headers=headers
    )
    code_link = get_link(response.json()['code'])
    assert response.status_code == 200
    assert response.json()['long'] == long_link
    assert long_link == code_link


def creat_option_link_custom():
    long_link = "https://hh.ru/search/vacancyitems_on_page=50"
    customer_code = 'hh-ru'
    body = {
        "long": long_link,
        "custom": customer_code
    }
    headers = {"Content-Type": "application/json"}
    response = requests.post('https://gotiny.cc/api', json=body, headers=headers)
    code_link = get_link(response.json()['code'])
    assert response.status_code == 200
    assert response.json()['code'] == customer_code
    assert response.json()['long'] == long_link
    assert long_link == code_link


def creat_option_link_usefallback():
    long_link = "https://hh.ru/search/vacancyitems_on"
    customer_code = new_link(long_link + 'test')
    body = {
        "long": long_link,
        "custom": customer_code,
        "useFallback": False
    }
    headers = {"Content-Type": "application/json"}
    response = requests.post('https://gotiny.cc/api', json=body, headers=headers)
    assert response.status_code == 200
    assert response.json()['error']['code'] != customer_code


def get_link_text():
    long_link = 'https://hh.ru/search/vacancyitems_on_page=50'
    new_code = new_link(long_link)
    response = requests.get(f'https://gotiny.cc/api/{new_code}')
    assert response.text == long_link


def get_link_json():
    long_link = 'https://hh.ru/search/vacancyitems_on_page=50'
    new_code = new_link(long_link)
    response = requests.get(f'https://gotiny.cc/api/{new_code}?format=json')
    assert response.json()['long'] == long_link
