# : followed by a legal formatting type, like .2f which means fixed point number with 2 decimals
price = 67
txt = f"The price of {price:.2f} euros"
print(txt)

txt = f"The price is {67:.2f} dollars" # Formatting the value directly in the string
print(txt)

txt = f"The price is {20 * 67:.2f} dollars" # I can do math operation inside the placeholders {}
print(txt)

price = 67
tax = 0.25
txt = f"The price is {price + (price * tax)} dollars"
print(txt)

price = 47
txt = f"It is very {'Expensive' if price > 50 else 'Cheap'}"

print(txt)

apples = "apples"
txt = f"I love {apples.upper()}"
print(txt)

def myconverter(x):
  return x * 0.3048

txt = f"The plane is flying at a {myconverter(67)} kilometer altitude" # I can use returned values of a function inside the placeholders
print(txt)

price = 67000
txt = f"The price is {price:,} dollars" # thousand separator
print(txt)

# Using the format() method. this one is slower and is preffered to use 'f' instead
quantity = 3
itemno = 67
price = 67
myorder = "I want {} dieces of item {} at {:.2f} dollars"
print(myorder.format(quantity, itemno, price))

age = 22
name = "tet"
txt = "His name is {1}. {1} is {0} years older than me." # age, age, name
print(txt.format(age, name))

myorder = "I have a {carname}, it is a {model}."
print(myorder.format(carname = "SAD", model = "TA")) # named indexes

# None is a special constant in Python that represents the absence of a value.
x = None
print(x)
print(type(x))

result = None
if result is None:
  print("No result yet")
else:
  print("Result is ready")

print(bool(None))

def myfunc():
  x = 1 
        # no return

x = myfunc()
print(x) # non will be printed since the function didn't return anything

print("Enter your INPUT:")
test = input()
print(f"here is your input: {test}")

test = input("Enter your name:") # input() can have a string containing a value, this is a parameter that allows to enter a message instead of using print in a different line
print(f"Hello {test}")


# casting x to a float value from the input

y = True
while y == True:
  x = input("Enter a number:")
  try:
    x = float(x)
    y = False
  except:
    print("Wrong input, please try again.")

print(f"Here's your number {x}")

# --- Environments ---
'''
Think of a virtual environment as a separate container for each Python project. Each container:

Has its own Python interpreter
Has its own set of installed packages
Is isolated from other virtual environments
Can have different versions of the same package
'''