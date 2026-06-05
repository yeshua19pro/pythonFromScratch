#When you create an object from a class, it inherits all the variables and functions defined inside that class.
# A Class is like an object constructor, or a "blueprint" for creating objects.

class Test:
    x = 10

p1 = Test()
print(p1.x)

# to delete objects
del p1

# class definitions cannot be empty but I can use the pass statement as a placeholder

class PlaceHolder:
    pass

p2 = PlaceHolder()
print(type(p2))


# Create a class
class Person:
  def __init__(self, name, age): # this is used to set properties and do operation while creating an object from the class
    self.name = name
    self.age = age

  def greet(self):
    print(f"Hello, my name is {self.name}")

# Create an object
p1 = Person("Jhon", 36)

# Call the greet method
p1.greet()

# --- Class without init method ---
class Person:
  pass

p1 = Person()
p1.name = "Tobias"
p1.age = 25

print(p1.name)
print(p1.age)

class Person:
  def __init__(self, name, age=18): # default value will be 18
    self.name = name
    self.age = age

p1 = Person("Emil")
p2 = Person("Tobias", 25) # here age will be 25, this overrides the age = 18 default parameter

print(p1.name, p1.age)
print(p2.name, p2.age)

class Person:
  species = "Human" # Class property, changing it will affect all objects

  def __init__(self, name):
    self.name = name # Instance property, this belongs to each object created and can be different from one instance to another


class Person:
  def __init__(self, name):
    self.name = name

p1 = Person("Tobias")

p1.age = 25
p1.city = "Oslo" # adding new propertie

print(p1.name)
print(p1.age)
print(p1.city) # city is not part of the definition of the person class

class Calculator:
  def add(self, a, b):
    return a + b

  def multiply(self, a, b):
    return a * b

calc = Calculator()
print(calc.add(5, 3))
print(calc.multiply(4, 7)) # methods can be invoked inside the print

# __str__() method is a special method that controls what is returned when the object is printed

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return f"{self.name} ({self.age})" # when used print (object) __str__ method will be called

p1 = Person("Tobias", 36)
print(p1)