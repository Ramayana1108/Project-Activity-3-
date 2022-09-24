# This example requires the requests library be installed.  You can learn more
# about the Requests library here: https://pypi.org/project/requests/
from requests import get
import json

# API used https://ip-api.com/
loc = get('http://ip-api.com/json/?fields=8729')

# The json.dumps method converts a Python object to a JSON formatted string.
responseString = json.dumps(loc.json())

# Call json.loads(json_object_string) to convert a json_object_string to a dictionary. Use dictionary indexing to access a value associated with a specific key.

# if you need to parse a JSON string into a native Python object, you have to use the json.loads() method
pythonObject = json.loads(responseString)

# This print statement prints the value of the query/isp/city/country key
print("\n IPv4/IPv6: " + pythonObject['query'])

print("\n ISP: " + pythonObject['isp'])

print("\n City: " + pythonObject['city'])

print("\n Region: " + pythonObject['regionName'])

print("\n Country: " + pythonObject['country'])