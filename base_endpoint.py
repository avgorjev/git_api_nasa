import os
import datetime


API_KEY = os.environ['api_key']
url = f"https://api.nasa.gov/planetary/apod?api_key={API_KEY}"
payload = {}
headers = {}

class DateTime:

    def date_now(self):
        self.date = datetime.date.today().strftime("%Y-%m-%d")
        return self.date

    def date_tomorrow(self):
        self.date =  (datetime.date.today() + datetime.timedelta(days=1)).strftime("%Y-%m-%d")
        return self.date

    def day_now(self):
        self.date = datetime.date.today().strftime("%d")
        return self.date

    def date_anyday(self, year:int, month:int, day:int):
        self.date = datetime.datetime(year, month, day).strftime("%Y-%m-%d")
        return self.date

    def date_now_response(self):
        self.date = datetime.date.today().strftime("%b %d, %Y")
        return self.date

    def date_anyday_response(self, year:int, month:int, day:int):
        self.date = datetime.datetime(year, month, day).strftime("%b %d, %Y")
        return self.date


url_date_0 = f"https://api.nasa.gov/planetary/apod?api_key={API_KEY}&date={DateTime().date_now()}"

def url_date(date):
    return f"https://api.nasa.gov/planetary/apod?api_key={API_KEY}&date={date}"

def url_count(count):
    return f"https://api.nasa.gov/planetary/apod?api_key={API_KEY}&count={count}"

