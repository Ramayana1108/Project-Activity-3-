import requests
import os

API_KEY = os.environ["API_KEY"]

def test_httpStatusCodeEqual200():
    response = requests.get("http://api.ipapi.com/check?access_key={API_KEY}")
    assert response.status_code == 200