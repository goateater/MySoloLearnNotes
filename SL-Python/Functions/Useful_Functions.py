# Useful Functions


# String Functions
# Python contains many useful built-in functions and methods to accomplish common tasks.



# Some examples:

print("join - joins a list of strings with another string as a separator. ")
print(", ".join(["spam", "eggs", "ham"]))
# prints "spam, eggs, ham"

print()

print("replace - replaces one substring in a string with another.")
print("Hello ME".replace("ME", "world"))
# prints "Hello world"

print()

print("startswith and endswith - determine if there is a substring at the start and end of a string, respectively.")
print("This is a sentence.".startswith("This"))
# prints "True"

print()

print("This is a sentence.".endswith("sentence."))
# prints "True"

print()

print("To change the case of a string, you can use lower and upper.")
print("This is a sentence.".upper())
# prints "THIS IS A SENTENCE."

print()

print("AN ALL CAPS SENTENCE".lower())
# prints "an all caps sentence"

print()

print("The method split is the opposite of join, turning a string with a certain separator into a list.")
print("spam, eggs, ham".split("a"))
# prints "['spam', 'eggs', 'ham']"

print()

print("You can also join previously split lists with following code:")
a = ["spam", "eggs", "ham"]
b = ["grave", "disease"]


def join(x):
    return (" and ".join(x))


# joins (x) list with " i "
def split(x):
    return (join(x).split(" and "))


# splits previously joined list


print(join(a))
print(join(b))

print(split(a))
print(split(b))

print()

print("A useful application of .join method for getting digits sorted in ascending/descending order in an integer:")


def desc(number):
    return int("".join(sorted(str(number))))


def asc(number):
    return int("".join(sorted(str(number), reverse=True)))


print(desc(53716), asc(53716))

print()

# Numeric Functions

print("To find the maximum or minimum of some numbers or a list, you can use max or min.")
print("Min: ", min(1, 2, 3, 4, 0, 2, 1))

print()

print("")
print("Max: ", max([1, 4, 9, 2, 5, 6, 8]))

print()

print("To find the distance of a number from zero (its absolute value), use abs.")
print(abs(-99))

print()

print("To round a number to a certain number of decimal places, use round.")
# Think of the second argument to round being the number of places after the decimal point, so 0 is to the nearest unit, minus numbers are before the units

print(round(42.6))
print(round(3.14159))  # whole number so 3
print(round(3.14159, 2))  # 2 decimal places so 3.14
print(round(44, 0))  # whole number so 44
print(round(44, -1))  # nearest ten so 40
print(round(46, -1))  # confirms this rounds to nearest ten so 50
print(round(5995, -3))  # nearest thousand so 6000

print()

i = 98765.4321
print(round(i))
print(round(i, 1))
print(round(i, 2))
print(round(i, 3))
print(round(i, 4))
print(round(i, -1))
print(round(i, -2))
print(round(i, -3))
print(round(i, -4))

print()

print("To find the total of a list, use sum.")
print(sum([1, 2, 3, 4, 5]))

print()

a = min([sum([11, 22]), max(abs(-30), 2)])  # 33 and 30 -- so the answer is 30
print(a)

print("Let's break this down a little")
print(
    "So, the sum of 11 and 22 is 33, The absolute value of -30 is 30, Between 30 and 2, 30 is bigger,  Now we are left with a=min([33,30])")
print("Therefore, a = 30")

print()

# List Functions
# Often used in conditional statements, all and any take a list as an argument,
# and return True if all or any (respectively) of their arguments evaluate to True (and False otherwise).
# The function enumerate can be used to iterate through the values and indices of a list simultaneously.

nums = [55, 44, 33, 22, 11]

if all([i > 5 for i in nums]):
    print("All larger than 5")

if any([i % 2 == 0 for i in nums]):
    print("At least one is even")

for v in enumerate(nums):
    print(v)

print()

# For the .enumerate function, you can specify what index number you want to start with. i.e.
for v in enumerate(nums, -1):
    print(v)

print()

# Depending on what kind of output you want, below are some examples

# outputs only the elements of nums
for v in nums:
    print(v)

print()

# outputs tuples with indexes
for v in enumerate(nums):
    print(v)

print()

# if you need to put this data in dictionary, it is easier with tuples
dict = {}
for v in enumerate(nums):
    key = v[0]
    dict[key] = v[1]
print(dict)

print()

nums = [-1, 2, -3, 4, -5]
if all([abs(i) < 3 for i in nums]):
    print(1)
else:
    print(2)

# To understand this question, first solve the negative value, I.e
# abs(-1) = 1
# abs(-3) = 3
# abs(-5) = 5
# Therefore we have:
# nums=[1,2,3,4,5]
# Then the conditions:
# all abs is not less than 3, so the program print 2.

