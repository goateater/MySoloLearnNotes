# More Types

# None

# The None object is used to represent the absence of a value.
# It is similar to null in other programming languages.
# Like other "empty" values, such as 0, [] and the empty string, it is False when converted to a Boolean variable.
# When entered at the Python console, it is displayed as the empty string.

# None is a SPECIAL VALUE that says "no object here". Things like "if" simply interpret that to mean False.
# You can assign None to variables, as you can with other values, but you don't have to.


print (None == None)
print(None)

print()

print('Also, note the following code with its output.')
print()

if None:
    print("None got interpreted as True")
else:
    print("None got interpreted as False")


# The None object is returned by any function that doesn't explicitly return anything else.

def some_func():
   var = ("HI")
   print(var)


var = some_func()
print(var)


foo = print()
print(foo)
if foo == None:
    print(1)
else:
    print(2)