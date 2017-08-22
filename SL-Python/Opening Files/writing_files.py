# Writing Files
# To write to files you use the write method, which writes a string to the file.
# For Example:

file = open("newfile.txt", "w")
file.write("This has been written to a file")
file.close()

file = open("newfile.txt", "r")
print(file.read())
file.close()

print()

# When a file is opened in write mode, the file's existing content is deleted.
file = open("newfile.txt", "r")
print("Reading initial contents")
print(file.read())
print("Finished")
file.close()

print()

file = open("newfile.txt", "w")
file.write("Some new text")
file.close()

print()

file = open("newfile.txt", "r")
print("Reading new contents")
print(file.read())
print("Finished")
file.close()

# Try It Yourself

# Result:
# >>>
# Reading initial contents
# some initial text
# Finished
# Reading new contents
# Some new text
# Finished
# >>>

print()

# The write method returns the number of bytes written to a file, if successful.

msg = "Hello world!"
file = open("newfile.txt", "w")
print(msg)
amount_written = file.write(msg)
print(type(amount_written))
print(amount_written)
file.close()

print()

file = open("newfile.txt", "r")
print(file.read())
file.close()

print()

# Working with Files

# It is good practice to avoid wasting resources by making sure that files are always closed after they have been used.
# One way of doing this is to use try and finally.
# This ensures that the file is always closed, even if an error occurs.

try:
    f = open("newfile.txt")
    print(f.read())
finally:
    f.close()

print()

# Finally block won't work properly if FileNotFoundError occurred. So... we can make another try~except block in finally:

try:
    f = open("filename.txt")
    print(f.read())
except FileNotFoundError:
    f = open("filename.txt", "w")
    f.write("The file has now been created")
    f.close()
    f = open("filename.txt", "r")
    print(f.read())
    f.close()
    # print("No such file or directory")
finally:
    try:
        f.close()
    except:
        print("Can't close file")

# Or we can force our program to open our py file. Like this:

try:
    f = open("filename.txt")
    print(f.read())
except FileNotFoundError:
    print("No such file or directory")
    f = open(__file__, "r")  # open itself
finally:
    f.close()

# In other cases when we catch FileNotFoundError f.close() makes error too (and program will stop).

# An alternative way of doing this is using "with" statements.
# This creates a temporary variable (often called f), which is only accessible in the indented block of the with statement.

with open("filename.txt") as f:
    print(f.read())

# The file is automatically closed at the end of the with statement, even if exceptions occur within it.


