# List Comprehensions


# List comprehensions are a useful way of quickly creating lists whose contents obey a simple rule.
# For example, we can do the following:
# List comprehensions are inspired by set-builder notation in mathematics.

cubes = [i**3 for i in range(5)]
print("cubes:", cubes)

nums = [i*2 for i in range(10)]
print("nums: ", nums)

# Explanation
# range 5 means from 0 to 4, giving (0, 1, 2, 3, 4.) making 5 in total, and the key is x**3. ** means power of
# so, this is what the code does below
# 0**3= 0×0×0= 0
# 1**3= 1×1×1= 1
# 2**3= 2×2×2= 8
# 3**3= 3×3×3= 27
# 4**3= 4×4×4= 64

# A list comprehension can also contain an if statement to enforce a condition on values in the list.
# Example:
evens=[i**2 for i in range(10) if i**2 % 2 == 0]
print("evens:", evens)

# On another note, you can add as many 'if's as you want!
# Example
evens_odds = [i**2 for i in range(10) if i**2 % 2 == 0 if i**2 % 3 == 0]
print("evens and odds:", evens_odds)

# The below will cause Memory Errors
# Trying to create a list in a very extensive range will result in a MemoryError.
# This code shows an example where the list comprehension runs out of memory.


# even = [2*i for i in range(10**100)] # 10**100 is also known as a googol
# print(even)

# This issue is solved by generators, which are covered in the next module.
