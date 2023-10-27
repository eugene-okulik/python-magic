# Для тестирования возьмем небольшое API сервиса сокращения ссылок: https://github.com/robvanbakel/gotiny-api
# Нужно простестировать все перечисленные в спецификации функции:
import requests
import pytest
import random
import string


# перед запуском всех тестов распечатывалось "Start testing", а по завершении всех тестов - "Testing completed"
# используется, например, для подключения к базе данных и запускается с того места в сессии, где это подключение нужно
@pytest.fixture(scope='session')
def start_end_session():
    print('\nStart testing')
    yield
    print('\nTesting completed')


# перед каждым тестом распечатывалось "before test", а после каждого теста - "after test"
# используется, например, для подключения к базе данных и запускается только для этой def
@pytest.fixture(scope='function')
def start_end_test():
    print('\nbefore test')
    yield
    print('\nafter test')


# создает новый 'custom'
@pytest.fixture
def create_new_code():
    random_str = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(10))
    body = {"long": "https://www.wildberries.by/catalog?fcolor=10824234&fdlvr=120&fsupplier=71316&page=1&search=%D0%",
            "custom": random_str,
            "useFallback": False
            }
    response = requests.post('https://gotiny.cc/api', json=body)
    return response.json()[0]["code"]


# Создание ссылки без дополнительных опций
# помечаем тест любым тэгом для удобства запуска '-m critical', но надо создать pytest.ini
# также можно запустить '-m "not critical"'
@pytest.mark.critical
#  Тест на создание ссылки оформлен так, чтобы он тестировал 3 разные ссылки с помощью parametrize
@pytest.mark.parametrize('urls',
                         ['https://www.wildberries.by/catalog?search=snake%20thai%20balm&tail-location=SNS',
                          '//www.wildberries.by/catalog?search=snake%20thai%20balm&tail-location=SNS',
                          '12345667string'
                          ]
                         )
def test_create_new_link_no_options(start_end_session, start_end_test, urls):
    body = {"input": urls}
    response = requests.post('https://gotiny.cc/api', json=body)
    assert response.status_code == 200
    assert response.json()[0]["long"] != "https://www.wildberries.by/catalog?fcolor=10824234&fdlvr=120&page=1"


# Создание ссылки с использованием опции custom (https://github.com/robvanbakel/gotiny-api#options)
def test_create_new_link_custom(create_new_code, start_end_test):
    body = {"long": "https://www.wildberries.by/catalog?fcolor=10824234&fdlvr=120&fsupplier=71316&page=1&search=%D0%",
            "custom": create_new_code
            }
    response = requests.post('https://gotiny.cc/api', json=body)
    assert response.status_code == 200


# Создание ссылки с использованием опций custom и useFallback
def test_create_new_link_custom_fallback(create_new_code, start_end_test):
    body = {"long": "https://www.wildberries.by/catalog?fcolor=10824234&fdlvr=120&fsupplier=71316&page=1&search=%D0%",
            "custom": create_new_code,
            "useFallback": False
            }
    response = requests.post('https://gotiny.cc/api', json=body)
    assert response.status_code == 200


# Получение длинной ссылки в виде текста (https://github.com/robvanbakel/gotiny-api#resolve-gotiny-link)
@pytest.mark.medium  # помечаем тест любым тэгом для удобства запуска '-m medium', но надо создать pytest.ini
def test_obtain_long_link(create_new_code, start_end_test):
    response = requests.get(f'https://gotiny.cc/api/{create_new_code}')
    assert response.status_code == 200
