# Dictionaries

# Dictionaries are data structures used to map arbitrary keys to values.
# Lists can be thought of as dictionaries with integer keys within a certain range.
# Dictionaries can be indexed in the same way as lists, using square brackets containing keys.
# Each element in a dictionary is represented by a key:value pair.

# Example:

ages = {"Dave": 24, "Mary": 42, "John": 58}
print(ages["Dave"])
print(ages["Mary"])

print()

# Trying to index a key that isn't part of the dictionary returns a KeyError.

primary = {
  "red": [255, 0, 0],
  "green": [0, 255, 0],
  "blue": [0, 0, 255],
}

print("Red is" , type(primary["red"]))

print()

# print(primary["yellow"])

# As you can see, a dictionary can store any types of data as values.
# An empty dictionary is defined as {}.

# test = { }
# print(test[0])

# Only immutable objects can be used as keys to dictionaries.
# Immutable objects are those that can't be changed.
# So far, the only mutable objects you've come across are lists and dictionaries.
# Trying to use a mutable object as a dictionary key causes a TypeError.

# This will work
good_dict = {
  1: "one two three",
}

print(good_dict[1])

print()

# This will not
#bad_dict = {
#  [1, 2, 3]: "one two three",
#}

#print(bad_dict[1,2,3])

# Dictionary Functions
# Just like lists, dictionary keys can be assigned to different values.
# However, unlike lists, a new dictionary key can also be assigned a value, not just ones that already exist.

squares = {1: 1, 2: 4, 3: "error", 4: 16,}
print(squares)
squares[8] = 64
squares[3] = 9
print(squares)

print()

# Something a little tricky
# What you've here is hierarchical nested Key-Value mapping passed on to the print function as an argument.
#So, you'd start start out first by solving the inner embedded Dictionary mapping call, primes[4], which maps to the value 7.
# And then, this 7 is rather a key to the outer Dictionary call, and thus, primes[7] would map to 17.


primes = {1: 2, 2: 3, 4: 7, 7:17}
print(primes[primes[4]])


print()


# To determine whether a key is in a dictionary, you can use in and not in, just as you can for a list.
# Example:
nums = {
  1: "one",
  2: "two",
  3: "three",
}
print(1 in nums)
print("three" in nums)
print(4 not in nums)

print()

# A useful dictionary method is get.
# It does the same thing as indexing, but if the key is not found in the dictionary it returns another specified value instead ('None', by default).

pairs = {1: "apple",
  "orange": [2, 3, 4],
  True: False,
  None: "True",
}

print(pairs.get("orange"))
print(pairs.get(7))
print(pairs.get(True))
print(pairs.get(12345, "not in dictionary")) # returns an alternate value instead of the default None, if they key does not exist.
print(pairs.get(None))

print()
# What is the result of the code below?
fib = {1: 1, 2: 1, 3: 2, 4: 3}
print(fib.get(4, 0) + fib.get(7, 5))

