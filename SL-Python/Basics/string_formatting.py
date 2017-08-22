# String Formatting

# So far, to combine strings and non-strings, you've converted the non-strings to strings and added them.
# String formatting provides a more powerful way to embed non-strings within strings.
# String formatting uses a string's format method to substitute a number of arguments in the string.
# Example:


nums = [4, 5, 6, 7]
msg = "Numbers: {0} {1} {2} {3}". format(nums[0], nums[1], nums[2], nums[3])
msg1 = "Numbers {0} {1} {2}". format(nums[0], nums[1], nums[2])
msg2 = "Numbers: {0} {1} {2}". format(nums[2], nums[1], nums[3])
print(msg)
print(msg1)
print(msg2)

# Each argument of the format function is placed in the string at the corresponding position, which is determined using the curly braces { }.
# Basically, in "Numbers: {0} {1}".format(nums[0], nums[1]), the nums[0] represents numbers in the list.
# So you can replace with, for example, "Numbers: {0} {1}".format(6, 7). This would lead to Numbers: 6 7.
# The numbers in the curly braces represent the order in the format method.
# So its "format([position 0], [position 1]) that correspond to the numbers in the curly braces: {0} {1}
# So numbers inside curly brackets{} are simply indexes of elements inside .format() bracket.

print("{0}{1}{0}".format("abra", "cad"))
print("{0} {1} {0}".format("abra", "cad")) # with spaces between the braces will cause the strings to be spaced out

# String formatting can also be done with named arguments.
# Example:
a = "{x}, {y}".format(x=5, y=12)
print(a)

print()

# The positional arguments should be placed before the keyword arguments (x,y etc), so u can access them in any order like below..
a = "{0}, {1}, {x}, {y}, {2}, {3}".format(1, 3, 33, 44, x=5, y=7)
print(a)

print()


# Clever string formatting using the random module
from random import randint
greetings = ["Hello","Howdy","You smell funny"]
title = ["Human.", "Trump!" , "Maid."]
greeting = "{x}, {y}".format(x=greetings[randint(0,2)], y=title[randint(0,2)])
print(greeting)

print()

str="{c}, {b}, {a}".format(a=5, b=9, c=7)
print(str)