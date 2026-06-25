'''
The key function for working with files in Python is the open() function.
The open() function takes two parameters; filename, and mode.
'''

# --- Modes ---
'''
"r" - Read - Default value. Opens a file for reading, error if the file does not exist
"a" - Append - Opens a file for appending, creates the file if it does not exist
"w" - Write - Opens a file for writing, creates the file if it does not exist
"x" - Create - Creates the specified file, returns an error if the file exists
"t" - Text - Default value. Text mode
"b" - Binary - Binary mode (e.g. images
'''
try:
    f = open("demofile.txt") # "r" for read, and "t" for text are the default values
    # f = open("demofile.txt", "rt") #both are the same rt = read text
    print(f.read()) # The open() function returns a file object, which has a read() method for reading the content of the file

    # if the location of the file is different use something like f = open("D:\\folder\welcome.txt")

except:
    print("File doesn't exists")


with open("demofile.txt") as f: # with automatically closes the files
  print(f.read()) # It is a good practice to always close the file when I'm done with it

f = open("demofile.txt")
print(f.readline())
f.close()

with open("demofile.txt") as f:
  print(f.read(5)) # this just returns 5 characters from the file

# to return a single line I can use:
with open("demofile.txt") as f:
  print(f.readline())

# using a for loop as next
cont = 1
with open("demofile.txt") as f:
  for x in f:
    print(f"the line is {cont}")
    print(x)
    cont += 1
 