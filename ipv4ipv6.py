# This example requires the requests library be installed.  You can learn more
# about the Requests library here: http://docs.python-requests.org/en/latest/
from requests import get
import json

loc = get('http://ip-api.com/json/?fields=66846719')

# The json.dumps method converts a Python object to a JSON formatted string.
responseString = json.dumps(loc.json())

# Call json.loads(json_object_string) to convert a json_object_string to a dictionary. Use dictionary indexing to access a value associated with a specific key.

# if you need to parse a JSON string into a native Python object, you have to use the json.loads() method
pythonObject = json.loads(responseString)

# This print statement prints the value of the "query" key
print("\n Your IP address is: " + pythonObject['query'] + "\n")

# This print statement prints the string 
print(json.dumps(pythonObject, sort_keys=True, indent=4))

# This print statement prints the formatted Python dictionary
# print(pythonObject)