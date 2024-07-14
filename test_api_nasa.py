import requests
from base_endpoint import (DateTime,
                            url,
url_date_0,
url_date,
url_count,
payload,
headers
                           )

base_date = DateTime()


def test_apod_today():
    response = requests.request("GET", url, headers=headers, data=payload)
    assert response.status_code == 200
    assert response.json()['date'] == base_date.date_now()

def test_apod_oldest():
    date = base_date.date_anyday(1995,6, 16)
    response = requests.request("GET", url_date(date), headers=headers, data=payload)
    assert response.status_code == 200
    assert response.json()['date'] == date


def test_apod_more_oldest():
    date = base_date.date_anyday(1995,6, 15)
    response = requests.request("GET", url_date(date), headers=headers, data=payload)
    assert response.status_code == 400
    assert response.json()['msg'] == f'Date must be between Jun 16, 1995 and {base_date.date_now_response()}.'


def test_apod_more_newest():
    date = base_date.date_tomorrow()
    response = requests.request("GET", url_date(date), headers=headers, data=payload)
    assert response.status_code == 400
    assert response.json()['msg'] == f'Date must be between Jun 16, 1995 and {base_date.date_now_response()}.'


def test_apod_one_count():
    count = 1
    response = requests.request("GET", url_count(count), headers=headers, data=payload)
    assert response.status_code == 200
    assert len(response.json()) == count


def test_apod_zero_count():
    count = 0
    response = requests.request("GET", url_count(count), headers=headers, data=payload)
    assert response.status_code == 400
    assert response.json()['msg'] == 'Count must be positive and cannot exceed 100'


def test_apod_count_is_100():
    count = 100
    response = requests.request("GET", url_count(count), headers=headers, data=payload)
    assert response.status_code == 200
    assert len(response.json()) == count


def test_apod_count_is_101():
    count = 101
    response = requests.request("GET", url_count(count), headers=headers, data=payload)
    assert response.status_code == 400
    assert response.json()['msg'] == 'Count must be positive and cannot exceed 100'