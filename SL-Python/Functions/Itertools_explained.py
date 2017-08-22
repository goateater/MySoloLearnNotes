# itertools


# The module itertools is a standard library that contains several functions that are useful in functional programming.
# One type of function it produces is infinite iterators.
# The function count counts up infinitely from a value.
# The function cycle infinitely iterates through an iterable (for instance a list or string).
# The function repeat repeats an object, either infinitely or a specific number of times.
# Example:

from itertools import count

for i in count(3):
    print(i)
    if i >=11:
        break

print()

# count has two arguments: count(x, y) where x is a start value and y is the increment/decrement pace (with y being a positive or negative number, respectively).

for i in count(4,5):
    print (i)
    if i >=24:
        break

print()

for i in count(20,-3):
    print (i)
    if i <=11:
        break

print()


import itertools

for i in dir(itertools):
    print (i)

print()

# There are many functions in itertools that operate on iterables, in a similar way to map and filter.
# Some examples:
# takewhile - takes items from an iterable while a predicate function remains true;
# chain - combines several iterables into one long one;
# accumulate - returns a running total of values in an iterable.

from itertools import accumulate, takewhile, chain

nums = list(accumulate(range(8))) # 1 + 2 + 3 + 4 + 5 + 6 + 7
print(nums)
print()
print(list(takewhile(lambda x: x<= 6, nums)))
print()
print(list(chain([1,3,2], [3,5,9])))
print()
print(list(chain(["Huri","daas"], ["GOvinda"])))

print()
nums = [2, 4, 6, 7, 9, 8]
a = takewhile(lambda x: x%2==0, nums)
print(list(a))


# There are also several combinatoric functions in itertool, such as product and permutation.
# These are used when you want to accomplish a task with all possible combinations of some items.
# Example:

print()

from itertools import product, permutations

# product returns all possible combinations of two (or possibly more) inputs
# permutation returns all possible combinations of all the different values in one input (list).

letters = ("A", "B", "C")
print(list(product(letters, range(2))))
print(list(permutations(letters)))

print()

a={1, 2}
print(list(product(range(3), a)))
print(len(list(product(range(3), a))))

print()
print("To better see how product from itertool is iterating through the range:")
for i in range(3):
    print(i)