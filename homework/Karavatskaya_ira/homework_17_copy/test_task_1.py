import json
import pytest
import requests
import random
import string


@pytest.fixture(scope='session')
def hello():
    print('Start testing')
    yield
    print("Testing completed")


@pytest.fixture(scope='function')
def start():
    print('before test')
    yield
    print("after test")


@pytest.fixture
def create_new_code():
    random_str = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(10))
    body = {"long": "https://www.amazon.com/HyperX-Cloud-III-Wireless-Microphone/dp/"
                    "B0CBQXGZ85?ref_=ast_sto_dp&th=1&psc=1",
            "custom": random_str,
            "useFallback": False
            }
    response = requests.post('https://gotiny.cc/api', json=body)
    return response.json()[0]["code"]


@pytest.mark.critical
def test_new_cus_link(create_new_code, hello, start):
    body = {"long": "https://www.amazon.com/HyperX-Cloud-Stinger-Comfortable-Noise-Cancellation/dp/B01L2ZRYVE/ref="
                    "sr_1_1?_encoding=UTF8&content-id=amen1.sym.12129333-2117-4490-9c17-6d31baf0582a&keywords="
                    "gaming+headsets&pd_rd_r=c858eb0c-1587-4d2e-acc0-16e8645cc1c3&pd_rd_w=ViCoV&pd_rd_wg="
                    "hvssK&pf_rd_p=12129333-2117-4490-9c17-6d31baf0582a&pf_rd_r=NRJHR3H8EPEE4Q4HVJH7&qid=1699014110"
                    "&sr=8-1",
            "custom": create_new_code
            }
    response = requests.post('https://gotiny.cc/api', json=body)
    assert response.headers['Content-Type'] != "application/json"
    assert response.status_code == 200


@pytest.mark.parametrize('urls',

                         ['https://m.media-amazon.com'
                          '/images/I/static/js/static/js/2-6efad138c3244c9c2fc4.chunk.js.map.js',
                          'https://www.amazon.com/dp/B099Z8HLHT?ref=MARS_NAV_desktop_firetab_shopdvcs_tablet_hd8',
                          'https://www.amazon.com/'
                          'All-new-Amazon-Stick-bundle-Doorbell/dp/'
                          'B0CHNBGYC3?pf_rd_r=1GPRJZ26K1FFK2Z09RQF&pf_rd_t=Events&pf_rd_i=deals&pf_rd_p'
                          '=3ae53701-83d5-4296-b2fe-99795b97c27b&pf_rd_s='
                          'slot-14&ref=dlx_deals_gd_dcl_img_0_504540b7_dt_sl14_7b'
                          ]
                         )
def test_new_link(urls, start, hello):
    body = {'input': urls}
    response = requests.post(
        "https://gotiny.cc/api", json=body)

    assert response.status_code == 200
    assert response.json()[0]['long'] != "https://www.amazon.com/s?k=gaming+headsets&_encoding=" \
                                         "UTF8&content-id=amzn1.sym.12129333-2117-4490-9c17-6d31baf0582a&pd_rd_r" \
                                         "=c858eb0c-1587-4d2e-acc0-16e8645cc1c3&pd_rd_w=ViCoV&pd_rd_wg=hvssK&pf_rd_p" \
                                         "=12129333-2117-4490-9c17-6d31baf0582a&pf_rd_r=" \
                                         "NRJHR3H8EPQF4Q4HVJH7&ref=pd_gw_unk"


def test_new_full_link(start, hello):
    body = {"long": "https://www.amazon.com/stores/HyperX/page/C3BFE396-3717-4B59-A6EA-0A070E7654D1?ref_=ast_bln"}
    response = requests.post('https://gotiny.cc/api', json=body)
    assert response.status_code == 200
    assert response.json()[0]["long"] != 'https://www.amazon.com/' \
                                         'HyperX-Cloud-Stinger-Comfortable-Noise-Cancellation/' \
                                         'dp/B01L2ZRYVE/ref=sr_1_1?_encoding=UTF8&content-id' \
                                         '=amzn1.sym.12129333-2117-4490-9c17-6d31baf0582a&keywords' \
                                         '=gaming+headsets&pd_rd_r=c858eb0c-1587-4d2e-acc0-16e8645cc1c3&pd_rd_w' \
                                         '=ViCoV&pd_rd_wg=hvssK&pf_rd_p=12129333-2117-4490-9c17-6d31baf0582a&pf_rd_r' \
                                         '=NRJHR3H8EPQF4Q4HVJH7&qid=1699014110&sr=8-1'


@pytest.mark.medium
def test_link_as_text(hello, start):
    url = "https://gotiny.cc/api/br7a3x"
    payload = {}
    headers = {}
    response = requests.get(url, headers=headers, data=payload)
    assert response.status_code == 200
