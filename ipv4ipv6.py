# Import API access key and specific fields or types of information
from api import apiKey, fieldsResponse
# This example requires the requests library be installed.  You can learn more about the Requests library here: https://pypi.org/project/requests/
from requests import get
# JSON encoder and decoder information here: https://docs.python.org/3/library/json.html
import json

# tkinter used to display a window screen
from tkinter import *

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


# Backlog: save output into text file
# Creating a text file with a write function
file = open("ipOutput.txt", "w")

# Writing text file with the output
file.write(
f"""IPv4/IPv6: {pythonObject['ip']}
City: {pythonObject['city']}
Region: {pythonObject['region_name']}
Country: {pythonObject['country_name']}""")
file.close()


# Backlog: Display user requested data
# Creating the window
root = Tk()
root.title('DEVASC Project')

# Height and Width of the app
app_width = 500
app_height = 500

# Finding the center of user screen
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width/2) - (app_width/2)
y = (screen_height/2) - (app_height/2)


root.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')


# Text shown
label = Label(root, text=f"""
    Project 4
    IPv4/IPv6: {pythonObject['ip']}
    City: {pythonObject['city']}
    Region: {pythonObject['region_name']}
    Country: {pythonObject['country_name']}""")
label.pack(pady=20)


# Render the app
root.mainloop()

