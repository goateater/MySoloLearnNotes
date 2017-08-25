# Inheritance

# Inheritance provides a way to share functionality between classes.
# Imagine several classes, Cat, Dog, Rabbit and so on. Although they may differ
# in some ways (only Dog might have the method bark), they are likely to be
# similar in others (all having the attributes color and name).


# This similarity can be expressed by making them all inherit from a superclass Animal, which contains the shared functionality.
# To inherit a class from another class, put the superclass name in parentheses after the class name.
# Example:

class Animal:
    def __init__(self, name, color):
        self.name = name
        self.color = color

class Cat(Animal):
    def purr(self):
        print("Purr...")

class Dog(Animal):
    def bark(self):
        print("Woof!")

fido = Dog("Fido", "brown")
print(fido.color)
fido.bark()

print()

kitty = Cat("Ginger", "rainbow")
print(kitty.color)
kitty.purr()


# A class that inherits from another class is called a subclass.
# A class that is inherited from is called a superclass.
# If a class inherits from another with the same attributes or methods, it overrides them.
print()


class Wolf:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def bark(self):
        print("Grr...")


class Dog(Wolf):
    def bark(self):
        print("Woof")


husky = Dog("Max", "Grey")
print(husky.name + " is " + husky.color)
husky.bark()
print()
dire = Wolf("Ghost", "White")
print(dire.name + " is " + dire.color)
dire.bark()

# In the example above, Wolf is the superclass, Dog is the subclass.

print()

class A:
  def method(self):
    print(1)

class B(A):
  def method(self):
    print(2)

B().method()


# Q: Why is the last line "B().method()" and NOT simply "B.method()"???
# A: Because class A has NO ATTRIBUTES at all!

# Class B inherited from class A, so the attributes+methods of class A got "copy & pasted" to B.
# Hence, class B has NO ATTRIBUTES at all, just like class A, simply the method "method()" that prints out 1,
# which in turn is overwritten by "method()" that prints out 2.

# Now, suppose that instead of the FINAL line of code in the question's example, we've got the following two lines,
# where right side of first line has empty parentheses just because class B has NO ATTRIBUTES at all.

# some_instance = B()
# some_instance.method()

# "B().method()" just simplifies the above 2 linea of code into a single one really - DRY principle I guess.
# Hopefully, it now makes sense why we have the final line of code in the question's example as ""B().method()" rather than "B.method()".


# Inheritance can also be indirect.
# One class can inherit from another, and that class can inherit from a third class.
# Example:

print()


class A:
    def method(self):
        print("A method")


class B(A):
    def another_method(self):
        print("B method")


class C(B):
    def third_method(self):
        print("C method")


c = C()
c.method()
c.another_method()
c.third_method()

# However, circular inheritance is not possible.


# Class A has NO ATTRIBUTES at all, but it does have a SINGLE method,
# namely "method()", which takes no arguments at all and prints out "A method".

# Attributes + Methods of class A are inherited by class B, so it means that the
# attributes + Methods of class A get "copy & pasted" onto class B.
# Hence, now class B is equipped with now 1 but rather 2 Methods:

# "method()" which prints "A method" AND "another_method()" which prints "B method".

# Next, Attributes + Methods of class B (2 Methods and no attributes whatsoever) get
# "copy & pasted" onto class C. Hence, class C now has 3 Methods and no attributes,
# and these 3 Methods which are the following:

# "method()" which prints "A method", AND "another_method()" which prints "B method", AND "third_method()" which prints "C method".

# So, class C comes equipped with ALL these 3 ↑ Methods actually! :)
# Hence, why we're totally ALLOWED to use absolutely ANY of these 3 Methods for
# any instance/object of the class C, such as the instance"c" they've got there in the example.

class A:
    def a(self):
        print(1)


class B(A):
    def a(self):
        print(2)


class C(B):
    def c(self):
        print(3)


c = C()
c.a()

print()

# The function super is a useful inheritance-related function that refers to the parent class.
# It can be used to find the method with a certain name in an object's superclass.
# Example:

class A:
    def spam(self):
        print(1)


class B(A):
    def spam(self):
        print(2)
        super().spam()


B().spam()


# super().spam() calls the spam method of the superclass.
