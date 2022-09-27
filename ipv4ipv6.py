
# Import API access key and specific fields or types of information
from api import apiKey, fieldsResponse
# This example requires the requests library be installed.  You can learn more about the Requests library here: https://pypi.org/project/requests/
from requests import get
# JSON encoder and decoder information here: https://docs.python.org/3/library/json.html
import json

# IPAPI documentation: https://ipapi.com/documentation
apiUrl = get(f"http://api.ipapi.com/check?access_key={apiKey}&fields={fieldsResponse}")

# The json.dumps method converts a Python object to a JSON formatted string.
responseString = json.dumps(apiUrl.json())

# Call json.loads(json_object_string) to convert a json_object_string to a dictionary. Use dictionary indexing to access a value associated with a specific key.

# If you need to parse a JSON string into a native Python object, you have to use the json.loads() method--this is now a Python dictionary.
pythonObject = json.loads(responseString)

# Multiline f-string print the value of the ip/city/region/country field. 
# Read more here: https://docs.python.org/3/whatsnew/3.6.html#whatsnew36-pep498 and https://stackoverflow.com/questions/10112614/how-do-i-create-a-multiline-python-string-with-inline-variables
print(f"""
    IPv4/IPv6: {pythonObject['ip']}
    City: {pythonObject['city']}
    Region: {pythonObject['region_name']}
    Country: {pythonObject['country_name']}""")