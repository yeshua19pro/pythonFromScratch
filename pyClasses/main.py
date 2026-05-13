# --- Casting ---
a = int (10)
x = float (a)
print(x)
b = bool(0)

# --- Formating ---
print(f"the value of x is {x}")
print(f"{x:.4f}")

numbers = [1, 2, 3, 4, 5]

if (contar := len(numbers)) > 3:
    print(f"List has {contar} elements")

'''
 --- Lists --- Lists are one of 4 built-in data types in Python used to store collections of data, the other 3 are Tuple, Set, and Dictionary
'''
# --- Unpack ---
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits 
print(x)
print(y)
print(z)
print(fruits)
print(len(fruits))

# --- Lists can contain different data types ---
multi_list = ["abc", 34, True, 40, "male"]
print(multi_list)
print(type(multi_list))

# --- List Constructor ---
cons_list = list(("Apple", "Banana", True))
print(cons_list)

"""
- List is a collection which is ordered and changeable. Allows duplicate members.
- Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
- Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
- Dictionary is a collection which is ordered** and changeable. No duplicate members.
- *Set items are unchangeable, but you can remove and/or add items whenever you like.
"""

# --- Negativa indexing --- Negative indexing means start from the end -1 refers to the last item, -2 refers to the second last item etc.
print(cons_list[-1])
print(cons_list[:2])
print(cons_list[-2:-1])

# --- Change list values
cons_list[0] = ["blackcurrant", "watermelon", "platano"]
cons_list.insert(3, "Balabalabala") #  inserts an item at the specified index:
cons_list.append("orange") # Add an item to the end
cons_list.extend(multi_list) # Add at the end of the list the elements of another list
thistuple = ("kiwi", "orange")
cons_list.extend(thistuple) # Add a tuple to the end
cons_list.remove("Balabalabala") # Remove the first element that matches
cons_list.pop(1) # Removes the element in the index 1
del cons_list[1] # Removes the element in the index 1
cons_list.clear # Clear the list content
print(cons_list)

# --- Loop a List ---
for x in cons_list: # Creates an object that iterates through the list
    print(x, type(x))

[print(x,'Hola') for x in cons_list] # Another way to do the above

for i in range(len(cons_list)): # This is used to iterate like a java for loop
    print(cons_list[i])

j = 0 # I need to initialize the variable that is going to loop through the list
while j < len(cons_list):
    print(cons_list[j])
    j += 1

newlist = []

for x in fruits:
  if "a" in x: # if any of the items in fruits has an 'a' it will be added to the new list
    newlist.append(x)

new_list = [x for x in fruits if "a" in x] # is the same as above Syntax: newlist = [expression for item in iterable if condition == True]
# new_list = [x for x in fruits if x != "Banana"]
# newlist = [x for x in fruits] # With no conditional, since it can be omited 
# newlist = [x for x in range (10)] # Using a range
# newlist = [x for x in range (10) if x < 5] # Using a range
# newlist = [x.upper() for x in fruits] # Setting the values to upper case before it ends
# newlist = ['hello' for x in fruits] # Set all values to hello
# newlist = [x if x != "banana" else "orange" for x in fruits] # It will create a new list with the same value in the position, except for the position that contains "banana"

# --- Sorting a List ---
fruits.sort() # Sorting ascending by default
print(cons_list)
fruits.sort(reverse = True) # Sorting descending sort() method is case sensitive, resulting in all capital letters being sorted before lower case letters:
fruits.sort(key = str.lower)
print(fruits)
# The function will return a number that will be used to sort the list (the lowest number first):  based on how close the number is to 50:
def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)
thislist.reverse() # Invert the list order
print(thislist)

# --- Copying a List ---
"""
You cannot copy a list simply by typing list2 = list1, because: list2 will only be a reference to list1,
and changes made in list1 will automatically also be made in list2.
Use the built-in List method copy() to copy a list.
"""

mylist = thislist.copy()
print(mylist)
mylist2 = list(thislist) # This do the same as .copy()
print(mylist2)
mylist3 = thislist[:] # This is also a .copy()
print(mylist3)

# --- Joining Lists ---
mylist4 = mylist + mylist2
print(mylist4)

mylist5 = [1, 2, 3]
for x in mylist3:
    mylist5.append(x)

print(mylist5)
mylist6 = list(mylist4)
mylist6.extend(mylist5)
print(mylist6)

