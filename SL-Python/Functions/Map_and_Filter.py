# Map and Filter

# The built-in functions map and filter are very useful higher-order functions that operate on lists (or similar objects called iterables).
# The function map takes a function and an iterable as arguments, and returns a new iterable with the function applied to each argument.

# MAP

def add_five(x):
    return x + 5

nums = [11, 22, 33, 44, 55]
result = list(map(add_five, nums))
print(result)

# We could have achieved the same result more easily by using lambda syntax.

nums = [11, 22, 33, 44, 55]

result = list(map(lambda x: x+5, nums))
print(result)

# To convert the result into a list, we used list explicitly.

# Filter
# The function filter filters an iterable by removing items that don't match a predicate (a function that returns a Boolean).
nums = [11, 22, 33, 44, 55]
res = list(filter(lambda x: x%2==0, nums))
print(res)

# Like map, the result has to be explicitly converted to a list if you want to print it.
print ()

def add_five(x):
    return x+5
num=[11,22,33,44,55]
result=list(map(lambda x: x+5,num))
res=tuple(filter(lambda x: x%2==0,num))
oui=tuple(map(lambda x: x%2==0,num))

print(result)
print(res)
print(oui)

print ()

# The same result with list comprehension:
nums= [11, 22, 33, 44, 55]

print([x for x in nums if x%2==0])
print ([x + 5 for x in [11, 22, 33, 44, 55]])
