# Recursion


# Recursion is a very important concept in functional programming.
# The fundamental part of recursion is self-reference - functions calling themselves.
# It is used to solve problems that can be broken up into easier sub-problems of the same type.

# A classic example of a function that is implemented recursively is the factorial function,
# which finds the product of all positive integers below a specified number.

# For example, 5! (5 factorial) is 5 * 4 * 3 * 2 * 1 (120).
# To implement this recursively, notice that 5! = 5 * 4!, 4! = 4 * 3!, 3! = 3 * 2!, and so on. Generally, n! = n * (n-1)!.
# Furthermore, 1! = 1.
# This is known as the base case, as it can be calculated without performing any more factorials.
# Below is a recursive implementation of the factorial function.
# For further information on Recursion - https://youtu.be/Mv9NEXX1VHc


def factorial(x):
    if x == 1:
        return 1
    else:
        return x * factorial(x - 1)


print(factorial(5))

# The base case acts as the exit condition of the recursion.

# If you enter a negative number with the code above, the code will crash
# However, below, the code takes that into consideration, and uses a try and except clause to mitigate that bug.


print()


# Using another method, using assert

def factorial(x):
    assert x >= 0, "Enter a positive number"
    assert round(x) == x, "Enter an integer"
    if x == 1 or x == 0:
        return 1
    else:
        return x * factorial(x - 1)


print(factorial(5))

# Using list comprehension to do this
listit = [n * factorial(n - 1) for n in range(1, 6)]
print(int(listit[-1]))

# Recursive functions can be infinite, just like infinite while loops.
# These often occur when you forget to implement the base case.
# Below is an incorrect version of the factorial function.
# It has no base case, so it runs until the interpreter runs out of memory and crashes.
# The base case for a factorial is 1, since no base case.. it will not function correctly


# def factorial(x):
#  return x * factorial(x-1)

# print(factorial(5))

# >>>
# RuntimeError: maximum recursion depth exceeded
# >>>

print()


# Will show you step by step how this works recursively

def factorial(x):
    if x == 1:
        return 1
    else:
        print(str(x) + " * factorial(" + str(x) + "-1)")
        return x * factorial(x - 1)


num = input("Factorial of: ")
print(num + "\n")
print(factorial(int(num)))

print()


# Recursion can also be indirect.
# One function can call a second, which calls the first, which calls the second, and so on.
# This can occur with any number of functions.
# Example:

def is_even(x):
    if x == 0:
        return True
    else:
        return is_odd(x - 1)


def is_odd(x):
    return not is_even(x)


print(is_odd(17))
print(is_even(23))

print()


def is_even(x):
    print("call to is_even where x = " + str(x))
    if x == 0:
        print("since x is 0 we hit our base and return True for this call of is_even")
        return True
    else:
        print("x is not 0 on this call of is_even so we check if the number below is odd")
        return is_odd(x - 1)


def is_odd(x):
    print("call to is_odd where x = " + str(x))
    print("we check if this current value is the opposite of even")
    resultFromIsEven = is_even(x)
    print("our result from is_even with x = " + str(x) + " comes back as " + str(resultFromIsEven))
    result = not (resultFromIsEven)
    print("so the call of is_odd where x = " + str(x) + " is returned as " + str(result))
    return result


print(is_odd(7))
# print(is_even(23))
