import requests
import pytest

@pytest.fixture()
def num():
    return 3

def test_get_link_text(before_after, new_link):
    long_link = new_link['long']
    response = requests.get(f"https://gotiny.cc/api/{new_link['code']}")
    assert response.text == long_link


def test_num(num):
    print(f'\n{num}')
    assert num == num