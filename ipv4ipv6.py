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

# Backlog: save output into text file
def saveToText():
    while True:
        saveOutput = input("\nSave output? [Y/N] (overwrite): ")
        if saveOutput == "Y" or saveOutput == "y":
            # Creating a text file with a write function
            file = open("ipOutput.txt", "w")
            match integerInput:
                case 1:
                    # Writing text file with the output
                    file.write(
                    f"""IPv4/IPv6: {pythonObject['ip']}""")
                    file.close()
                    print("Output saved as ipOutput.txt")
                    break
                case 2:
                    file.write(
                    f"""City: {pythonObject['city']}""")
                    file.close()
                    print("Output saved as ipOutput.txt")
                    break
                case 3:
                    file.write(
                    f"""Region: {pythonObject['region_name']}""")
                    file.close()
                    print("Output saved as ipOutput.txt")
                    break
                case 4:
                    file.write(
                    f"""Country: {pythonObject['country_name']}""")
                    file.close()
                    print("Output saved as ipOutput.txt")
                    break
                case _:
                    file.write(
f"""IPv4/IPv6: {pythonObject['ip']}
City: {pythonObject['city']}
Region: {pythonObject['region_name']}
Country: {pythonObject['country_name']}""")
                    file.close()
                    print("Output saved as ipOutput.txt")
                    break
        else:
            print("Exited application.")
            break

# Backlog: Display user requested data
print(f"""
    [ 1 ] IPv4/IPv6
    [ 2 ] City
    [ 3 ] Region
    [ 4 ] Country
    [ 5 ] Print all of the above \n""")

# A singleDigitInput() function to check for the integer input
def singleDigitInput():
    while True:
        integerInput = input("Enter an integer: ")
        if not integerInput.isnumeric():
            print("Please enter a single digit integer only. \n")
            continue
        integerInput = int(integerInput)
        if integerInput <= 5 and integerInput >= 1:
            return integerInput
        else:
            print("Value of integer is not a valid input, please try again. \n")

# Call for the single digit integer input to determine the output
integerInput = singleDigitInput()

match integerInput:
    case 1:
        print(f"""
    IPv4/IPv6: {pythonObject['ip']}""")
        saveOutput = saveToText()
    case 2:
        print(f"""
    City: {pythonObject['city']}""")
        saveOutput = saveToText()
    case 3:
        print(f"""
    Region: {pythonObject['region_name']}""")
        saveOutput = saveToText()
    case 4:
        print(f"""
    Country: {pythonObject['country_name']}""")
        saveOutput = saveToText()
    case _:
        print(f"""
    IPv4/IPv6: {pythonObject['ip']}
    City: {pythonObject['city']}
    Region: {pythonObject['region_name']}
    Country: {pythonObject['country_name']}""")
        saveOutput = saveToText()