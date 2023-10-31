import requests
import pytest
import random


@pytest.fixture(scope='session')
def start_stop():
    print("\nStart testing")
    yield
    print("\nTesting completed")


@pytest.fixture()
def before_after():
    print("\nbefore test")
    yield
    print("\nafter test")


@pytest.fixture()
def new_link():
    body = {
        "input": f"https://hh{random.randint(0, 999)}.ru/search/vacancyitems_on_page=50"
    }
    headers = {"Content-Type": "application/json"}
    response = requests.post(
        'https://gotiny.cc/api',
        json=body,
        headers=headers
    )
    return response.json()[0]


def get_link(cod_id):
    response = requests.get(f'https://gotiny.cc/api/{cod_id}')
    return response.text


@pytest.mark.critical
@pytest.mark.parametrize(
    'link',
    [
        'https://dzen.ru/news/rubric/personal_feed?issue_tld=ru&utm_referrer=dzen.ru',
        'https://www.apple.com/ru/shop/goto/help/sales_refunds',
        'https://www.levels.fyi/t/software-engineer/focus/testing-sdet?countryId=254&searchText=Irvine'
    ]
)
def test_creat_simple_link(link, start_stop, before_after):
    long_link = link
    body = {
        "input": long_link
    }
    headers = {"Content-Type": "application/json"}
    response = requests.post(
        'https://gotiny.cc/api',
        json=body,
        headers=headers
    )
    code_link = get_link(response.json()[0]['code'])
    assert response.status_code == 200
    assert response.json()[0]['long'] == long_link
    assert long_link == code_link


def test_creat_option_link_custom(before_after):
    unic_number = random.randint(0, 999)
    long_link = f"https://hh{unic_number}.ru/search/vacancyitems_on_page=50"
    customer_code = f'hh{unic_number}_ru'
    body = {
        "long": long_link,
        "custom": customer_code
    }
    headers = {"Content-Type": "application/json"}
    response = requests.post('https://gotiny.cc/api', json=body, headers=headers)
    code_link = get_link(response.json()[0]['code'])
    assert response.status_code == 200
    assert response.json()[0]['code'] == customer_code
    assert response.json()[0]['long'] == long_link
    assert long_link == code_link


@pytest.mark.medium
def test_creat_option_link_usefallback(before_after, new_link):
    long_link = new_link['long']
    customer_code = new_link['code']
    body = {
        "long": long_link,
        "custom": customer_code,
        "useFallback": False
    }
    headers = {"Content-Type": "application/json"}
    response = requests.post('https://gotiny.cc/api', json=body, headers=headers)
    assert response.status_code == 200
    assert response.json()['error']['code'] != customer_code


def test_get_link_text(before_after, new_link):
    long_link = new_link['long']
    response = requests.get(f"https://gotiny.cc/api/{new_link['code']}")
    assert response.text == long_link


def test_get_link_json(before_after, new_link):
    long_link = new_link['long']
    response = requests.get(f"https://gotiny.cc/api/{new_link['code']}?format=json")
    assert response.json()['long'] == long_link
