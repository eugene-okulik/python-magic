import requests
import pytest
import allure


def post(body):
    headers = {'Content-Type': 'application/json'}
    response = requests.post(
        'https://gotiny.cc/api',
        json=body,
        headers=headers
    )
    return response


def get_code_and_long_url(code):
    url = f'https://gotiny.cc/api/{code}?format=json'
    response = requests.get(url)
    return response.json()


@pytest.fixture(scope='session')
def setup_session():
    print("Start testing")
    yield
    print("Testing completed")


@pytest.fixture
def setup_test():
    print("Before test")
    yield
    print("After test")


@pytest.mark.parametrize("input_body, expected_long_url", [
    (
        {"input": "https://www.gismeteo.by/weather-vitebsk-4218/"},
        "https://www.gismeteo.by/weather-vitebsk-4218/"
    ),
    (
        {"long": "https://www.gismeteo.by/weather-vitebsk-4219/", "custom": "1test-gis"},
        "https://www.gismeteo.by/weather-vitebsk-4219/"
    ),
    (
        {"long": "https://www.gismeteo.by/weather-vitebsk-4220/", "custom": "2test-gis", "userFallback": "false"},
        "https://www.gismeteo.by/weather-vitebsk-4220/"
    ),
])
@allure.feature('Posts')
@allure.story('Links')
@pytest.mark.critical
def test_post_and_assertions(setup_session, setup_test, input_body, expected_long_url):
    with allure.step(f'Run post with inputs'):
        response = post(input_body)

    with allure.step(f'Check if the response status code is 200'):
        assert response.status_code == 200

    # Process the response JSON
    response_json = response.json()

    with allure.step('Check if the response contains at least one item'):
        assert len(response_json) >= 1

    # Extract the code from the response JSON
    code = response_json[0]["code"]

    # Construct the full URL by appending the code to "https://gotiny.cc/"
    full_url = f"https://gotiny.cc/{code}"

    # Check if the constructed URL redirects to the expected long URL
    redirect_response = requests.get(full_url, allow_redirects=False)
    with allure.step('302 is the HTTP status code for a temporary redirect'):
        assert redirect_response.status_code == 302
    with allure.step('Check expected long URL in Location header'):
        assert redirect_response.headers["Location"] == expected_long_url

    # Check GET request for code and long URL
    get_response = get_code_and_long_url(code)
    assert get_response["code"] == code
    assert get_response["long"] == expected_long_url
