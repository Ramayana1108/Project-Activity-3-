import requests
apiKey = "205ed62a0bee3bf828a4d4d98ecfd1c7"
fieldsResponse = "ip,country_name,city,region_name"

def test_httpStatusCodeEqual200():
    response = requests.get("http://api.ipapi.com/check?access_key={apiKey}&fields={fieldsResponse}")
    assert response.status_code == 200
