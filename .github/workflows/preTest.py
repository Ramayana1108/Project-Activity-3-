import requests
import os

# API_KEY = os.environ["API_KEY"]

def test_httpStatusCodeEqual200():
    response = requests.get("http://api.ipapi.com/check?access_key=205ed62a0bee3bf828a4d4d98ecfd1c7")
    assert response.status_code == 200
