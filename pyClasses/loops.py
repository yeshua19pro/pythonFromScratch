i = 0
while i < 10:
    # print(i)
    i += 1
    if(i == 3):
        #break # exits the loop
        continue
    print(i) # skips the 0 with the continue then starts in 1
print("done")

i = 0
while i < 6:
    print(i)
    i += 1
else:
    print("variable 'i' is no longer less than 6")

# --- For Loops ---
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

# Looping a string
str = "string"
for x in str:
    print(x)

# Break statement also in for loops
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break

# continue statement (does not print ban)
fruits = ["che", "ban", "arr","querr"]
for x in fruits:
  if x == "ban":
    continue
  print(x)

# range() function in loops

for x in range(10):
    print(x)

print("Start of range 5, 12")
for x in range(5, 12):
    print(x)

print("Start of range 2, 30 with increments of 2")
for x in range(2, 30, 2): #2 increments
  print(x)

for x in range(16):
  print(x)
else: 
  print("Else statement after for loop")

for x in range(16):
  if x == 13: break
  print(x)
else: # Else is not executed if a break statement is executed inside the for loop
  print("Finally finished!")

# Nested loops
a = ["0", "1", "2"]
d = ["0", "1", "2"]

for x in a:
  for y in d:
    print(x, y)

# Pass statement is used to skip empty loops (no logic)
for x in [0, 1, 2]:
  pass