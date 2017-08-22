

# SoloLearn Assertions Explanation
# =================================
#An assertion is a sanity-check that you can turn on or turn off when
#you have finished testing the program.

# An expression is tested, and if the result comes up false, an exception
# is raised. Assertions are carried out through use of the assert statement.

# Programmers often place assertions at the start of a function to check for valid input,
# and after a function call to check for valid output.



# Other Sources
# =============

# Source #1
# ==========
# Good wiki description explaining difference in usage of
# assert vs if-then or try-except type error handling.

# Look for the "Comparison with error handling" section of this wiki page

# https://en.m.wikipedia.org/wiki/Assertion_(software_development)

# Source #2
# ==========
# This link below has a great example and explaination about assert.
# http://www.tutorialspoint.com/python/assertions_in_python.htm




# print(assertions)

print(1)
assert 2 + 2 == 4
print(2)
assert 1 + 2 == 3
print(3)

# AssertionError exceptions can be caught and handled like any other exception using
# the try-except statement, but if not handled, this type of exception will terminate the program.

print()

try:
    x = 4
    y = 2
    assert x - y == 2, print("nope thats not right") # The second portion is an AssertionError
    print (x - y)
    assert x * y == 8, print("nope thats not right either") # The second portion is an AssertionError
    print (x * y)
except:
    print ("somethings wrong")
finally:
    print("Everything looks good!")