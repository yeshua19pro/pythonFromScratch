# Dates in python can be managed as object if we import it
import datetime
x = datetime.datetime.now()
print (x)

print(x.year)
print(x.strftime("%A"))

# Using a constructor
x = datetime.datetime(2009, 9, 5)
print(x.year)
print(x.strftime("%A"))

# --- Math ---
import math

x = min(5, 10, 25) # 5
y = max(5, 10, 25) # 25

print(x)
print(y)

x = abs(-7.25) # Absolute value in positive

print(x)

x = pow(4, 3) # 4 ^ 3

print(x)

x = math.sqrt(69) # Square root
print(x)

# The math.ceil() method rounds a number upwards to its nearest integer, and the math.floor() method rounds a number downwards to its nearest integer, and returns the result:
x = math.ceil(1.4)
y = math.floor(1.4)
print (x)
print (y)


# --- JSON !!!! ---
import json

# Parse Json to python dictionary:

x =  '{ "name":"John", "age":30, "city":"New York"}'

y = json.loads(x)

print(y["age"])

x = {
    "name" : "bruno",
    "age"  : "16",
    "city" : "pasto"
}

# parse Python to json
y = json.dumps(x)
print(y)

print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))

# Convert a Python object containing all the legal data types:

import json

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}
#json.dumps(x, indent=4) # define the number of idents
#print(json.dumps(x, indent = 2))

print(type(x["cars"]))
print(x["cars"])
print(json.dumps(x, indent=4, separators=(". ", " = "))) # You can also define the separators, default value is (", ", ": "), which means using a comma and a space to separate each object, and a colon and a space to separate keys from values:

# json.dumps(x, indent=4, sort_keys=True) # specify if the result will be sorted or not



# --- RegEx ---
import re

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt) # ^ starts with and *something$ ends with something 
print(x)

# The findall() function returns a list containing all matches.
txt = "The rain in Spain"
x = re.findall("ai", txt) # If no matches are found, an empty list is returned:
print(x)

'''
The search() function searches the string for a match, and returns a Match object if there is a match.
If there is more than one match, only the first occurrence of the match will be returned:
'''

txt = "The rain in Spain" 
x = re.search("\s", txt) # If no matches are found, the value None is returned


print("The first white-space character is located in position:", x.start())

# The split() function returns a list where the string has been split at each match:

txt = "The train to Spain"
x = re.split("\s", txt)
print(x)

# I can control the number of occurrences by specifying the maxsplit parameter
txt = "The train to Spain"
x = re.split("\s", txt, 1) # 1 is the max split
print(x)

# The sub() function replaces the matches with the text of my choice
txt = "The train to Spain"
x = re.sub("\s", "9", txt)
print(x)

txt = "The train to Spain"
x = re.sub("\s", "9", txt, 2) # Just replace the first 2 occurrences
print(x)

# A Match Object is an object containing information about the search and the result. If there is no match, the value None will be returned, instead of the Match Object.
'''
The Match object has properties and methods used to retrieve information about the search, and the result:

.span() returns a tuple containing the start-, and end positions of the match.
.string returns the string passed into the function
.group() returns the part of the string where there was a match
'''

txt = "The train to Spain"
#x = re.search(r"\bP\w+", txt) #P throws and error since it would be only if starts with P any word in the txt
#print(x.span())

txt = "The train to Spain"
x = re.search(r"\bS\w+", txt)
print(x.string) # Print the string passed into the function

txt = "The train to Spain dice"
x = re.search(r"\bS\w+", txt)
print(x.group()) # Print the part of the string where there was a match.

# Use the uninstall command to remove a package pip uninstall intrepik
# pip list shows all the packages installed

'''
The try block lets you test a block of code for errors.

The except block lets you handle the error.

The else block lets you execute code when there is no error.

The finally block lets you execute code, regardless of the result of the try- and except blocks.
'''

try:
  print(x)
except:
  print("qw variable has nothing in it")

# I can define as many exception blocks as you want, e.g. if you want to execute a special block of code for a special kind of error
try:
  print(x)
except NameError:
  print("Variable qw is not defined")
except:
  print("Something else went wrong")
else:
    print("watashiwa") #else is used to execute something when no error occurs
finally: #The finally block, if specified, will be executed regardless if the try block raises an error or not.
    print("Flet is no longer flet, is for fats, use capacitor instead")


# Conditional exception
'''
As a Python developer you can choose to throw an exception if a condition occurs.

To throw (or raise) an exception, use the raise keyword.
'''

x = -1

if x < 0:
    raise Exception ("Negative numbers are not allowed")