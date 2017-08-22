# List Slices
# ===========
# List slices provide a more advanced way of retrieving values from a list.
# Basic list slicing involves indexing a list with two colon-separated integers.
# This returns a new list containing all the values in the old list between the indices.

# Like the arguments to range, the first index provided in a slice is included in the result, but the second isn't.

squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(squares[2:6])
print(squares[3:8])
print(squares[0:1])

print()

# If the first number in a slice is omitted, it is taken to be the start of the list.
# If the second number is omitted, it is taken to be the end.
# Example:

blocks = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(blocks[:7])
print(blocks[7:])

# Slicing can also be done on tuples.

print()

# List slices can also have a third number, representing the step, to include only alternate values in the slice.
# The structure is : print(squares:[start,stop,step]).

squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(squares[::2])
print("here it is")
print(squares[2:8:3])

# [2:8:3] will include elements starting from the 2nd index up to the 8th with a step of 3.

print()

# Negative values can be used in list slicing (and normal list indexing).
# When negative values are used for the first and second values in a slice (or a normal index),
# they count from the end of the list.

# If a negative value is used for the step, the slice is done backwards.
# Using [::-1] as a slice is a common and idiomatic way to reverse a list.


squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(squares)
print("using a negative value to go backwards")
print(squares[::-1])
print(squares[1:-1])

# If you use [1:1] it will not result any number. Because the indexes are the same and the slice doesnt count the second index.

# If you put [1::] it will count from the  index 1 up to the last element, the whole rest of the list (including the last index).
# If you use [1:-1] it starts to count from the index 1 to the last index, hiding the last element like a standard slice.
# If you put [::-1], with two commas, it will result the whole list in reverse mode. Because the -1 as the third argument represents the reverse order.
# The first comma represents all the elements from the end to begin, and the second one represents all the elements from the begin to end, so it brings the whole list.


print()

print("An example of list slicing, using a negative step, starting at element 7 and going to element 5")
sqs = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(sqs[7:5:-1])

print()

# The slicing of a list takes three arguments separated by colon. they are optional.
# lower limit : upper limit : steps
# By default (if you don't specify) lower limit is at index 0, upper limit is at the last value and steps is +1
# Using ::-1 as in the example below means don't slice anything off but give in reverse order. (the -ve sign brought the reverse)


mylist = [1, 2, 3, 4]
print(mylist)
backwardslist = mylist[::-1]
print(backwardslist)

print()

# Same example using strings instead of integers
stringlist = "There can be only one!"
print(stringlist)
reverse_stringlist = stringlist[::-1]
print(reverse_stringlist)

print()
# Extended outlook on slicing by example below

squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(squares)
print("The output above is the original list for squares")
print()
print("List Slicing with several exammples below")
print(squares[2:6])
print(squares[3:8])
print(squares[0:1])
print(squares[::-1])
print(squares[::2])
print(squares[::-2])
print(squares[3:9:2])
print(squares[7:1:-1])
print(squares[1:8:3])