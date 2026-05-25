def my_func():
    print("hello world")

my_func()

# If a function doesn't have a return statement, it returns None by default
# Function definitions cannot be empty. Use pass to have a placeholder for future code

def sum(x, y):
    return x + y

print(sum(5,2))
#Default Parameter Values. If the function is called without an argument, it uses the default value

def roi_func (roi = int(4)):
    return roi

print(roi_func())
# I can also use the name of the variable
print(roi_func(roi = "4.5"))

# Positional arguments if , / is used it just allow positional arguments

def positional(name, /):
    return "Hello " + name

print(positional("Bruno"))

# Keyword only arguments
def keyword (* , arg):
    return "Hello args: " + arg

print(keyword(arg = "Key"))

# Arguments before / are positional-only, and arguments after * are keyword-only:
def my_function(a, b, /, *, c, d):
  return a + b + c + d

result = my_function(5, 10, c = 15, d = 20)
print(result)

# How to accept an unknow number of arguments

def args (*names): #accept any number of positional arguments
    return names

print(args(["Hola", "Como", "Estas"]))

# Maximum value and none return
def my_function(*numbers):
  print(type(numbers))
  print(numbers)
  if len(numbers) == 0:
    return None
  max_num = numbers[0]
  for num in numbers:
    if num > max_num:
      max_num = num
  return max_num

print(my_function(3, 7, 2, 9, 1))

# **kwargs parameter allows a function to accept any number of keyword arguments. Inside the function, kwargs becomes a dictionary containing all the keyword arguments:
def my_function(**myvar):
  print("Type:", type(myvar))
  print("Name:", myvar["name"])
  print("Age:", myvar["age"])
  print("All data:", myvar)

my_function(name = "Tobias", age = 30, city = "Bergen")

# Unpacking
def my_function(a, b, c):
  return a + b + c

numbers = [1, 2, 3]
result = my_function(*numbers) # Same as: my_function(1, 2, 3)
print(result)

# Unpacking dictionaries
def my_function(fname, lname):
  print("Hello", fname, lname)

person = {"fname": "Emil", "lname": "Refsnes"}
my_function(**person) 

# Global variables
def myfunc():
  # pyrefly: ignore [unknown-name]
  global x # The global keyword makes the variable global
  x = 300

myfunc()

# pyrefly: ignore [unknown-name]
print(x)


# Changing a global variable
x = 300 # Global variable

def myfunc():
  global x  #To change the value of a global variable inside a function, refer to the variable by using the global keyword:
  x = 200

myfunc()

print(x)

def myfunc1():
  x = "Jane"
  def myfunc2():
    nonlocal x
    x = "hello" 
  myfunc2()
  return x # Jane will be printed since nonlocal keyword, the variable will belong to the outer function

print(myfunc1())

'''
The LEGB Rule
Python follows the LEGB rule when looking up variable names, and searches for them in this order:

Local - Inside the current function
Enclosing - Inside enclosing functions (from inner to outer)
Global - At the top level of the module
Built-in - In Python's built-in namespace
Example
'''

# Decorators let you add extra behavior to a function, without changing the function's code.
# A decorator is a function that takes another function as input and returns a new function.

def changecase(func):
  def myinner(): #wrapper, this will get the real value of func and then applies the .upper() method HELLO SALLY, then the outer method returns the funcion result
    return func().upper()
  return myinner

@changecase
def myfunction():
  return "Hello Sally"

print(myfunction())

def changecaso(func): 
  def myinner(x): # Using params
    return func(x).upper()
  return myinner

@changecaso
def myfunction(nam):
  return "Hello " + nam # Hello John will be passed to changecaso, then change caso pass it to myinner func with the param X, 'nam' will be the param x

print(myfunction("John"))

# Alternative to avoid errors:
def changecase(func):
  def myinner(*args, **kwargs): # Secure the function with *args and **kwargs arguments
    return func(*args, **kwargs).upper()
  return myinner

@changecase # Sometimes the decorator function has no control over the arguments passed from decorated function
def myfunction(nam):
  return "Hello " + nam

print(myfunction("John"))

# decorator factory
def changecase(n): # Gets the decorator argument to remember it for the inner funcs
  def decorator_changecase(func):
    def myinner(): # Wrapper when I call "myfunction", this function will be called instead, I will need to add *Args or *Kwargs if I'm going to use arguments in "myfunction"
      if n == 1:
        a = func().lower() 
      else:
        a = func().upper()
      return a
    return myinner
  return decorator_changecase # Must return the decorator that changes the value

@changecase(3)
def myfunction():
  return "Hello Linus"

print(myfunction())


# --- Metadata --
# Functions in Python has metadata that can be accessed using the __name__ and __doc__ attributes.
def myfunction():
  return "torm"

print(myfunction.__name__)

def changecase(func):
  def myinner():
    return func().upper()
  return myinner

@changecase
def myfunction():
  return "Have a great day!"

print(myfunction.__name__+"1") # It will return "myinner" since myinner is the wrapper and the function that's going to be called at the end. "functools.wraps" import solves this

import functools

def changecase(func):
  @functools.wraps(func)
  def myinner():
    return func().upper()
  return myinner

@changecase
def myfunction():
  return "Have a great day!"

print(myfunction.__name__ + "2")

person1 = {
  "name": "John",
  "age": 36,
  "country": "Norway"
}