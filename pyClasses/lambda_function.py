# A lambda function is a small anonymous function.
#A lambda function can take any number of arguments, but can only have one expression.
# Add 10 to argument a, and return the result:

x = lambda a : a + 10
print(x(5)) # this sent the 5 parameter to the lambda expression (a : a + 10) this is the same that x = 'arg' + 10

x = lambda a, b : a * b
print(x(5, 6))

x = lambda a, b, c : a + b + c
print(x(5, 6, 7))

# using lambda expressions as a return value

def double_up (n):
    return lambda x : x * n

cuadrado = double_up(3) # cuadrado = 3
print(cuadrado)
print(cuadrado (3)) # cuadrado = X,  the parameter '3' is the 'n' in the function

# Lambda functions are commonly used with built-in functions like map(), filter(), and sorted().
# The map() function applies a function to every item in an iterable:

numbers = [ 1, 2, 3, 4, 5]
double = list(map(lambda x: x * 2, numbers)) # this will duplicate each value in numbers, where X is the array value in the index
print(double)

# The filter() function creates a list of items for which a function returns True:

numbers = [1, 2, 3, 4, 5, 6, 7, 8]
odd_numbers = list(filter(lambda x: x % 2 != 0, numbers)) # this will just return the values inside the list that complies with the expression,
print(odd_numbers)


#The sorted() function can use a lambda as a key for custom sorting:
students = [("Emil", 25), ("Tobias", 22), ("Linus", 28)]
sorted_students = sorted(students, key=lambda x: x[1]) # Sort a list of tuples by the second element:
print(sorted_students)


words = ["apple", "pie", "banana", "cherry"]
sorted_words = sorted(words, key=lambda x: len(x)) # sort strings by len
print(sorted_words)

# Recursion
x = 1
def tables(n):
    if (n<1):
        print("---- That's ALL! ----")
    else:
        for x in range (11):
            
            if(x == 0):
                pass
            else:
                value = n*(x)
                print(f"{n} * {x} = {value}")
            return tables (n-1)

tables (10)


# When yield is encountered, the function's state is saved, and the value is returned. The next time the generator is called, it continues from where it left off.

def generator():
    yield print("Hola 1")
    yield print("Hola 2")
    yield print("Hola 3")

for x in generator():
    print(x)

# Generators are memory-efficient because they generate values on-the-fly instead of storing everything in memory
# For large datasets, generators save memory
def large_sequence(n):
  for i in range(n):
    yield i

# This doesn't create a million numbers in memory
gen = large_sequence(1000000)
print(next(gen))
print(next(gen))
print(next(gen))

# Generator expressions
# List comprehension, it is used with brackets
list_comp = [x * x for x in range(5)]
print(list_comp)

# Gen expressions are used with parentheses
gen_exp = (x * x for x in range(5))
print(gen_exp)
print(list(gen_exp))

total = sum(x * x for x in range(10))
print(total)

# The close() method stops the generator:
def my_gen():
  try:
    yield 1
    yield 2
    yield 3
  finally:
    print("Generator closed")

gen = my_gen()
print(next(gen))
gen.close()

# send method
def echo_generator():
  while True:
    received = yield
    print("Received:", received)

gen = echo_generator()
next(gen) # Prime the generator
gen.send("Hello")
gen.send("World")

# Range function is an inmutable sequence of numbers, it has its own datatype called Range
# It is used with 1, 2 or 3 arguments as next (start, stop, step)

x = range(3, 10, 2) # this will jump numbers 2 by 2
# ranges can be sliced to extract a subsequence.
r = range(10) # this goes from 0 to 9, last number '10' is not included since the range starts at 0
print(r[2])
print(r[:3])
print(type(r))

# Test if the numbers 6 and 7 are present in a range, also called Membership Testing

r = range(0,10,2) 
print(6 in r)
print(7 in r)
# the len function can also be used with range types
print(len(r))

# Python doesn't support arrays, it used lists instead.

# Iterators, Technically, in Python, an iterator is an object which implements the iterator protocol, which consist of the methods __iter__() and __next__().
mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple) # converting a tuple in an iterator object

print(next(myit))
print(next(myit))
print(next(myit))
print(type(myit))

# Using strings
mystr = "banana"
myit = iter(mystr)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(type(myit))

# all classes have a function called __init__(), which allows you to do some initializing when the object is being created.
# The __iter__() method acts similar, you can do operations (initializing etc.), but must always return the iterator object itself.
# The __next__() method also allows you to do operations, and must return the next item in the sequence.

class MyNumbers:
  def __iter__(self): # Overrides the __iter__ function in the class "MyNumbers"
    self.variable_to_store_one = 1
    return self

  def __next__(self):
    x = self.variable_to_store_one
    self.variable_to_store_one += 1
    return x

myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))

# To prevent the iteration from going on forever, we can use the StopIteration statement.

class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    if self.a <= 20:
      x = self.a
      self.a += 1
      return x
    else:
      raise StopIteration # this will stops the loop for going on forever

myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
  print(x)