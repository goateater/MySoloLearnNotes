# Lambdas

# Creating a function normally (using def) assigns it to a variable automatically.
# This is different from the creation of other objects - such as strings and integers
# which can be created on the fly, without assigning them to a variable.
# The same is possible with functions, provided that they are created using lambda syntax.
# Functions created this way are known as anonymous.
# This approach is most commonly used when passing a simple function as an argument to another function.
# The syntax is shown in the next example and consists of the lambda keyword followed
# by a list of arguments, a colon, and the expression to evaluate and return.

def my_func(f, arg):
    return f(arg)


a = (my_func(lambda x: 2 * x * x, 5))
print(a)
# Lambda functions get their name from lambda calculus, which is a model of computation invented by Alonzo Church.

print()


# Lambda functions aren't as powerful as named functions.
# They can only do things that require a single expression - usually equivalent to a single line of code.

# named function
def polynomial(x):
    return x ** 2 + 5 * x + 4


print(polynomial(-4))

# lambda
print((lambda x: x ** 2 + 5 * x + 4)(-4))

# In the code above, we created an anonymous function on the fly and called it with an argument.
# The formula behind the problem is algebraically seen as x² + 5x + 4

# It is worked out in the following manner:
# x**2 + 5*x + 4 where x=(-4)
# =(-4)**2 + 5*(-4) + 4
# =16 + -20 + 4
# =0


# Lambda functions can be assigned to variables, and used like normal functions.
# Example
double = lambda x: x * 2
print(double(7))

# However, there is rarely a good reason to do this - it is usually better to define a function with def instead.

print()
triple = lambda x: x * 3
add = lambda x, y: x + y
print(add(triple(3), 4))