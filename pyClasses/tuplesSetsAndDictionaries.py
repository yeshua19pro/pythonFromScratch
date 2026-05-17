'''
Tuple items are ordered, unchangeable, and allow duplicate values 
the items have a defined order, and that order will not change.
we cannot change, add or remove items after the tuple has been created.
'''
tuples = ("Value 1", "Value 2", "Value 3", False)

print(tuples)
print(len(tuples))

# To create a tuple with 1 item it must have a comma

tuples = ("Single Value",)
print(type(tuples))
print(tuples)

# Tuple constructor with double parentesis

tuple_constructor = tuple(("Value 1", False, True))
print(tuple_constructor)

# I can do negative index with tuples as it was with lists

print(tuple_constructor[-1])
print(tuple_constructor[-3:-2])

if "Value 1" in tuple_constructor:
    print("yes it is")
else:
    print("No, it is not")

# Tuples are unchangable, but there's a walk around casting a tuple to a list
tuple_list = list(tuple_constructor)
tuple_list.append(True)
print(tuple_list)

# Adding values to a tuple

tuple_constructor += tuples
tuple_constructor += tuple(tuple_list)
print(tuple_constructor)

# Removing a tuple, since they can't be changed the 'clear' method doesn't exist, but the tuple can be complete removed with del
del tuple_constructor

# Unpacking a tuple
test_tuple = ("Apple", "Pine", "Spine")
x, y, z = test_tuple

print(x)
print(y)
print(z)

# If the tuple is way bigger than the variables, I can use an '*' to assign the remaining values to a variable
abc_tuple = ("Apple", "Pine", "Spine", "Colors", "Wak")
(a, b, *c) = abc_tuple

print(a)
print(b)
print(c)
# If the '*' is put in the middle for instance in the 'b' variable, it will assign all values, except the remaining values match the remaining variables
abc_tuple = ("Apple", "Pine", "Spine", "Colors", "Wak")
(a, *b, c) = abc_tuple

print(a)
print(b)
print(c)

# Looping a tuple
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)

# Using an index
for x in range(len(thistuple)):
    print(thistuple[x]+" Index: "+ f"{x}")

# Using a while
i = 0
while i < len(thistuple):
    print(thistuple[i] +f" Using while, index at: {i}")
    i += 1

# Join tuples, I can add '+' a tuple to another one, I can also multiply its content using '*'
