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
    return response.json()


@pytest.fixture()
def num():
    return 1
