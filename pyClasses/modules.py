# To use the code created in other python class I need to use the 'import' statement
from lambda_function import cuadrado
import functions

# You can create an alias when you import a module, by using the as keyword:
import lambda_function as lf
functions.my_function("Yashua", "Se")

print(functions.person1)

lf.cuadrado
print(cuadrado(1))

# built - in modules are several built-in modules in Python, which you can import whenever you like.
import platform

x = platform.system()
print(x)

# There is a built-in function to list all the function names (or variable names) in a module. The dir() function:
import platform

x = dir(platform)
print(x)

# Importing only what you need

from functions import person1 

print (person1["age"]) # Note: When importing using the from keyword, do not use the module name when referring to elements in the module. Example: person1["age"], not mymodule.person1["age"] 