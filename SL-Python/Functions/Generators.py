# Generators
# Generators are a type of iterable, like lists or tuples.
# Unlike lists, they don't allow indexing with arbitrary indices, but they can still be iterated through with for loops.
# They can be created using functions and the yield statement.


#  Yield is something like a 'break'.
# At return, a normal funtion stops and returns its value.
# With yield, it just returns a value and 'pause'.
# When you call the function again (in a loop or something), it continues where it was left.
# A normal function always starts at the beginning, every time.

# In short, yield is like a temporary return where the retuned value can be processed outside the function.

def countdown():
    i = 5
    while i > 0:
        yield i
        print(">", i)
        i -= 1


for i in countdown():
    print(i)

print()
# The yield statement is used to define a generator, replacing the return of a function to provide a result to its caller without destroying local variables.

# Done in a typical while loop, where it starts from the begining unlike using yield
i = 10
while i > 0:
    print(i)
    i -= 1

print()

# Due to the fact that they yield one item at a time, generators don't have the memory restrictions of lists.
# In short, generators allow you to declare a function that behaves like an iterator, i.e. it can be used in a for loop.
# In fact, they can be infinite!
# Example Below:

# def infinite_sevens():
#  while True:
#    yield 7

# for i in infinite_sevens():
#  print(i)

print("Finite generators can be converted into lists by passing them as arguments to the list function.")


def numbers(x):
    for i in range(x):
        if i % 2 == 0:
            yield i


# numbers_example = numbers([11])
my_nums = numbers(11)
my_nums2 = [x * x for x in [1, 2, 3, 4, 5]]  # Generator

for i in my_nums:
    print(i)

print()

print(list(numbers(11)))

print()

print(my_nums2)
print(list(my_nums2))
for i in my_nums2:
    print(i)

# Using generators results in improved performance, which is the result of the lazy (on demand) generation of values, which translates to lower memory usage.
# Furthermore, we do not need to wait until all the elements have been generated before we start to use them.
# 'yield' is similar to 'return' but 'yield' returns more than once during a call whereas 'return' returns only once.

print()

print("3 ways of doing this, per the last few lessons")


def numbers(x):
    for i in range(x):
        if i % 2 == 0:
            yield i


print("Using the numbers function:", list(numbers(11)))

print("List Comprehension:", list([x for x in range(11) if x % 2 == 0]))

print("Filter:", list(filter((lambda x: x % 2 == 0), range(11))))

print("And an example of map:")
print("Filter:", list(map((lambda x: x % 2 == 0), range(11))))

# A good video about understanding generators - https://www.youtube.com/watch?v=bD05uGo_sVI

print()


def make_word():
    word = ""
    for ch in "spam":
        word += ch
        yield word


print(list(make_word()))

