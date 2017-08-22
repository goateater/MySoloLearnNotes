# Decorators

# Decorators provide a way to modify functions using other functions.
# This is ideal when you need to extend the functionality of functions that you don't want to modify.
# Example:

def decor(func):
  def wrap():
    print("============")
    func()
    print("============")
  return wrap

def print_text():
  print("Hello world!")

decorated = decor(print_text)
decorated()


# We defined a function named decor that has a single parameter func.
# Inside decor, we defined a nested function named wrap.
# The wrap function will print a string, then call func(), and print another string.
# The decor function returns the wrap function as its result.
# We could say that the variable decorated is a decorated version of print_text - it's print_text plus something.
# In fact, if we wrote a useful decorator we might want to replace print_text with the decorated version
# altogether so we always got our "plus something" version of print_text.
# This is done by re-assigning the variable that contains our function:

print()

# Now print_text corresponds to our decorated version.
print_text = decor(print_text)
print_text()

print()

# In our previous example, we decorated our function by replacing the variable containing the function with a wrapped version.
def print_text():
  print("Hello world!")

print_text = decor(print_text)

# This pattern can be used at any time, to wrap any function.
# Python provides support to wrap a function in a decorator by pre-pending the function definition with a decorator name and the @ symbol.
# If we are defining a function we can "decorate" it with the @ symbol like:

@decor #this will call the decorator function
def print_text():
  print("Hello world!")

print_text()

# A single function can have multiple decorators.

print()

# To understand the last statement about multiple decorators above, try this:

def decor(func):
    def wrap():
        print("============")
        func()
        print("============")
    return wrap

def decor1(func):
    def wrap1():
        print("************")
        func()
        print("************")
    return wrap1

@decor
@decor1
def print_text():
    print("Hello world!")

print_text();


# Decorators can be used for many other purposes than 'decorating'
# Consider this code:

def basic(func):
 def modified():
  #x=int(input(':'))
  #y=int(input(':'))
  x = 4
  y = 8
  func(x,y)
 return modified

@basic
def ad(x,y):
 print(x+y)

@basic
def prd(x,y):
 print(x*y)

@basic
def diff(x,y):
 print(x-y)

ad()
prd()
diff()