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
  def __init__(self, firstname, lastname):
    self.firstname = firstname
    self.lastname = lastname

  def __str__(self):
    return f"{self.firstname} ({self.lastname})" # when used print (object) __str__ method will be called
  
  def printname(self):
    print(self.firstname, self.lastname)

p1 = Person("Tobias", 36)
print(p1)

# To create a class that inherits the functionality from another class, send the parent class as a parameter when creating the child class


class Student(Person):
  def __init__(self, fname, lname,year): #child's __init__() function overrides the inheritance of the parent's __init__() function.
   Person.__init__(self, fname, lname) #To keep the inheritance of the parent's __init__() function
   super().__init__(fname, lname) # function that will make the child class inherit all the methods and properties from its parent, I do not have to use the name of the parent element, it will automatically inherit the methods and properties from its parent.
   self.graduationyear = 2019 #hardcoded, I can add it to the def init instead
   # properties 


#x = Student("Mike", "Olsen")
#x.printname()
x = Student("Mike", "Olsen", 2019)
print(x)

# Create the Animal class
class Animal:
  def __init__(self, name):
    self.name = name

  def speak(self):
    print(self.name)

# Create the Dog class (inherits from Animal)
class Dog(Animal):
  def __init__(self, name):
    super().__init__(name)

# Create an object
d1 = Dog("Rex")
# Call the speak method
d1.speak()

# ---Polymorphism ---

class Vehicle:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Move!")

class Car(Vehicle):
  pass

class Boat(Vehicle):
  def move(self):
    print("Sail!")

class Plane(Vehicle):
  def move(self):
    print("Fly!")

car1 = Car("Ford", "Mustang")       #Create a Car object
boat1 = Boat("Ibiza", "Touring 20") #Create a Boat object
plane1 = Plane("Boeing", "747")     #Create a Plane object

for x in (car1, boat1, plane1): # as long as all methods inherit from vehicle they can use the move() function from its parent or the one overrided by them
  print(x.brand)
  print(x.model)
  x.move()

  # --- Encapsulation ---

  # in Python I can make properties private by using a double underscore __ prefix
  # for protected properties use a single underscore _ prefix
  #  A single underscore _ is just a convention. It tells other programmers that the property is intended for internal use, but Python doesn't enforce this restriction.
class Person:
  def __init__(self, name, age):
    self.name = name
    self.__age = age # Private property
  
  def get_age(self): # Getter in python
    return self.__age

  def set_age(self, age):
    self.__age = age

p1 = Person("Emil", 25)
print(p1.name)
#print(p1.__age) # This will cause an error unless I do Name mangling p1._Person__age
print(p1.get_age())

class Person:
  def __init__(self, name, salary):
    self.name = name
    self._salary = salary # Protected property

p1 = Person("Linus", 50000)
print(p1.name)
print(p1._salary) # Can access, but shouldn't

class Calculator:
  def __init__(self):
    self.result = 0

  def __validate(self, num):
    if not isinstance(num, (int, float)):
      return False
    return True

  def add(self, num):
    if self.__validate(num):
      self.result += num
    else:
      print("Invalid number")

calc = Calculator()
calc.add(10)
calc.add(5)
print(calc.result)
# calc.__validate(5) # This would cause an error

'''
Name Mangling
Name mangling is how Python implements private properties and methods.
When you use double underscores __, Python automatically renames it internally by adding _ClassName in front.
For example, __age becomes _Person__age.
'''

class Person:
  def __init__(self, name, age):
    self.name = name
    self.__age = age

p1 = Person("Emil", 30)

# This is how Python mangles the name:
print(p1._Person__age) # Not recommended!

# --- Inner Classes ---
'''
An inner class is a class defined inside another class. The inner class can access the properties and methods of the outer class.

Inner classes are useful for grouping classes that are only used in one place, making your code more organized.
'''
class Outer:
  def __init__(self):
    self.name = "Outer Class"

  class Inner:
    def __init__(self):
      self.name = "Inner Class"

    def display(self):
      print("This is the inner class")

outer = Outer()
print(outer.name)
inner = outer.Inner() # this calls the inner class to create the object
inner.display()
'''
Inner classes in Python do not automatically have access to the outer class instance.

If you want the inner class to access the outer class, you need to pass the outer class instance as a parameter:
'''

class Outer:
  def __init__(self):
    self.name = "Emil"

  class Inner:
    def __init__(self, outer): 
      self.outer = outer

    def display(self):
      print(f"Outer class name: {self.outer.name}")

outer = Outer()
inner = outer.Inner(outer)
inner.display()
# Inner classes are useful for creating helper classes that are only used within the context of the outer class
