# Functional Programming

# Introduction
print("Functional programming is a style of programming that (as the name suggests) is based around functions.")
print("A key part of functional programming is higher-order functions.")
print("We have seen this idea briefly in the previous lesson on functions as objects.")
print("Higher-order functions take other functions as arguments, or return them as results.")

print()


# The function apply_twice takes another function as its argument, and calls it twice inside its body.

def apply_twice(func, arg):
    return func(func(arg))


def add_five(x):
    return x + 5


print(apply_twice(add_five, 10))

# Two ways to explain how this works
# Number One:

"""
This is difficult for me to explain in words but here goes.

Understanding this problem requires a basic understanding of an algebraic concept called "composition of functions."
Think back to algebra class in high school where you had to evaluate f(g(3)). You first need to evaluate the inner function g, with an input of 3. The output/result of g(3) becomes the input of the outer function f. 

i.e.
given f(x) = x + 2    and    g(x) = 2x - 1    evaluate f(g(3))

First, evaluate g(3).
g(3) = 2(3) - 1
g(3) = 6 - 1
g(3) = 5

Second, take the result/output of g(3) which is 5, and plug it into the outer function f.

f(5) = (5) + 2
f(5) = 7

Thus, 
f(g(3)) = 7


Using that same understanding of composition of functions reconsider the problem below (I added line numbers).

1    def apply_twice(func, arg):
2       return func(func(arg))
3
4    def add_five(x):
5       return x + 5
6  
7    print(apply_twice(add_five, 10))

"""

# Number Two:

"""
1.def apply_twice(func, arg):
2.   return func(func(arg))
3.
4.def add_five(x):
5.    return x + 5
6.
7.print(apply_twice(add_five, 10))

We have to work backwards to understand this.
On line 7, we are calling the function “apply_twice”, which has two arguments: a call to another function ”add_five” and the number 10.
Now jump to line 1. It becomes “ def apply_twice(add_five,10).
Line 2 becomes “return func(add_five,10)”
Since a function is within the parentheses, right away we jump to another function, add_five, on line 4.
This becomes “def add_five(10):”
Line 5 becomes “return 10+5”. So now we have the value of 15.
Jumping back to line 2, we have “return func(15)”, which becomes “add_five(15)”.
We jump back to Line 4 and it becomes “def add_five(15):”, and line 5 becomes “return 15+5”, or 20.
So line 2 returns 20, which becomes the value of line 1, which is printed in line 7.

"""

print()


def test(func, arg):
    return func(func(arg))


def mult(x):
    return x * x


print(test(mult, 2))

print("Pure Functions")
print("==============")
print("Functional programming seeks to use pure functions.")
print("Pure functions have no side effects, and return a value that depends only on their arguments.")
print("This is how functions in math work..")
print("for example, The cos(x) will, for the same value of x, always return the same result.")
print("Below are examples of pure and impure functions.")

print()

print("Example of a pure function:")


def pure_function(x, y):
    temp = x + 2 * y
    return temp / (2 * x + y)


print(pure_function(5, 4))

print()

print("Example of an impure function:")
some_list = []


def impure(arg):
    some_list.append(arg)
    print(some_list)


(impure(100))
print("The function above is not pure, because it changed the state of some_list.")

print()

print("If the answer to all questions is 'yes', your function is pure.")
print()
print(
    "1. Does my function depend only on its arguments and nothing else? OR Does my function always return the same result given the same arguments?")
print("2. Can I run my function anywhere in the script without causing any trouble or side effects whatsoever?")
print("3. Can I run my function with the same arguments many times and still return the same result each time?")
print("4. Is it true that my function does not change anything outside it, but only returns something?")
print("5. Can my function be used by other functions or scripts with equal success?")

print()

print("Using pure functions has both advantages and disadvantages.")
print("Pure functions are:")
print("- easier to reason about and test.")
print("- more efficient.")
print("Once the function has been evaluated for an input, the result can be stored and referred")
print("to the next time the function of that input is needed, reducing the number of times the")
print("function is called. This is called 'memoization' - https://en.m.wikipedia.org/wiki/Memoization.")
print("- easier to run in parallel.")

print()

print("The main disadvantage of using only pure functions is that they majorly complicate")
print("the otherwise simple task of I/O, since this appears to inherently require side effects.")
print("They can also be more difficult to write in some situations.")
