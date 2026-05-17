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


# --- Sets ----
# A set is a collection which is unordered, unchangeable*, and unindexed.
test_set = {"set value 1", "set value 2", "set value 3"}
print(test_set)

# Set items can appear in a different order every time you use them, and cannot be referred to by index or key.
# Once a set is created, you cannot change its items, but you can remove items and add new items. Sets can't have duplicate values since it is not indexed
test_set = {"set value 1", "set value 2", "set value 3", "set value 3", "set value 3", "set value 3", True, 1, 0, False}
print(test_set)

'''
 0 and False  AND 1 and True are the same, only the 1st appearence will be displayed,
 for above, something like this: {0, True, 'set value 1', 'set value 2', 'set value 3'}
 Sets do also have constructor, can store multiple values and len() is used for the lenght of the data collection
'''

thisset = {"apple", "banana", "cherry"}

print("banana" in thisset)

for x in test_set:
    print(x)

# Adding values to a set
test_set.add("42")
print(test_set)

# Joining a set
test_set.update(thisset)
print(test_set)
test_set.update(tuple_list)
print(type(test_set))
print(type(tuple_list))
print(test_set)

test_set.remove("42")
test_set.discard("banana")# Discard fails silently
print(test_set)

test_set.clear()
print(test_set)
# del test_set
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
# Union and update both discards duplicate values
set3 = set1.union(set2) # I can also use | operator  set3 = set1 | set2 | setn
print(set3)

# Intersection can also be used with &
set4 = set3.intersection(set1) # Returns values that are present in both sets
set1 = set3.intersection_update(set2) #returns the value that are present in both sets (set 3 and 2) then updates the set1 with the new values instead of returning a new set
print(set4)

# Difference return the values that are not present in the other set. The difference update is similar to intersection in the sense of not returning a new set
# I can also use '-' operator. 
set7 = set2.difference(set4)
print("set 3")
print(set3)
print("set 4")
print(set4)
print(set7)

set1 = {"app", "anana", "cherry"}
set2 = {"google", "microsoft", "app"}

set3 = set1 - set2
print(set3)

# simetric_difference will keep the elements that are not present in both sets, symetric_difference_update also exists and is similar to the previous updates
# I can also use the '^' operator set3 = set1 ^ set2

set1 = {"app", "anana", "cherry"}
set2 = {"google", "microsoft", "app"}

set3 = set1.symmetric_difference(set2)
print(set3)

# frozenset is an inmutable version of a set
x = frozenset({"dia", "ana", "y"})
print(x)
print(type(x))