import requests
import datetime
import os

API_KEY = os.environ['api_key']



def date_now():
    return datetime.date.today().strftime("%Y-%m-%d")

def date_tomorrow():
    return (datetime.date.today() + datetime.timedelta(days=1)).strftime("%Y-%m-%d")


def day_now():
    return datetime.date.today().strftime("%d")


def date_anyday(year:int, month:int, day:int):
    return datetime.datetime(year, month, day).strftime("%Y-%m-%d")

def date_now_response():
    return datetime.date.today().strftime("%b %d, %Y")


def date_anyday_response(year:int, month:int, day:int):
    return datetime.datetime(year, month, day).strftime("%b %d, %Y")


url = f"https://api.nasa.gov/planetary/apod?api_key={API_KEY}"

url_date_0 = f"https://api.nasa.gov/planetary/apod?api_key={API_KEY}&date={date_now()}"

def url_date(date):
    return f"https://api.nasa.gov/planetary/apod?api_key={API_KEY}&date={date}"

def url_count(count):
    return f"https://api.nasa.gov/planetary/apod?api_key={API_KEY}&count={count}"

payload = {}
headers = {}


def test_apod_today():
    response = requests.request("GET", url, headers=headers, data=payload)
    assert response.status_code == 200
    assert response.json()['date'] == date_now()

def test_apod_oldest():
    date = date_anyday(1995,6, 16)
    response = requests.request("GET", url_date(date), headers=headers, data=payload)
    assert response.status_code == 200
    assert response.json()['date'] == date


def test_apod_more_oldest():
    date = date_anyday(1995,6, 15)
    response = requests.request("GET", url_date(date), headers=headers, data=payload)
    assert response.status_code == 400
    assert response.json()['msg'] == f'Date must be between Jun 16, 1995 and {date_now_response()}.'


def test_apod_more_newest():
    date = date_tomorrow()
    response = requests.request("GET", url_date(date), headers=headers, data=payload)
    assert response.status_code == 400
    assert response.json()['msg'] == f'Date must be between Jun 16, 1995 and {date_now_response()}.'


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