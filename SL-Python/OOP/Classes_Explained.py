# Classes
# =======

# We have previously looked at two paradigms of programming - imperative (using statements, loops, and functions as subroutines),
#  and functional (using pure functions, higher-order functions, and recursion).

# Another very popular paradigm is object-oriented programming (OOP).
# Objects are created using classes, which are actually the focal point of OOP.
# The class describes what the object will be, but is separate from the object itself.
# In other words, a class can be described as an object's blueprint, description, or definition.
# You can use the same class as a blueprint for creating multiple different objects.

# Classes are created using the keyword class and an indented block, which contains class methods (which are functions).
# Below is an example of a simple class and its objects.


# This code defines a class named Cat, which has two attributes: color and legs.
# Then the class is used to create 3 separate objects of that class.
# Tap Continue to learn more!

class Cat:
  def __init__(self, color, legs):
    self.color = color
    self.legs = legs

felix = Cat("ginger", 4)
rover = Cat("dog-colored", 4)
stumpy = Cat("brown", 3)

# If you have any problems learning OOP,
# try this: http://openbookproject.net/thinkcs/python/english3e/classes_and_objects_I.html#classes-and-objects-the-basics

# It is the third edition of "How to think like a computer scientist: Learning with Python 3".
# It is very well explained and clearly structured. Maybe it is a bit lengthy.
# But it will give you great explanations about what OOP is, why we need this and how to do it.

# Especially the examples in the link are so much more comprehensible than those in this SoloLearn tutorial.
# There is also a PDF-version available at:
# http://www.ict.ru.ac.za/Resources/cspw/thinkcspy3/thinkcspy3.pdf


# __init__
# =========
# The __init__ method is the most important method in a class.
# This is called when an instance (object) of the class is created, using the class name as a function.

# All methods must have self as their first parameter, although it isn't explicitly passed,
# Python adds the self argument to the list for you; you do not need to include it when you call the methods.
# Within a method definition, self refers to the instance calling the method.

# Instances of a class have attributes, which are pieces of data associated with them.
# In this example, Cat instances have attributes color and legs.
# These can be accessed by putting a dot, and the attribute name after an instance.
# In an __init__ method, self.attribute can therefore be used to set the initial value of an instance's attributes.
# Example:

class Cat:
  def __init__(self, color, legs, sex, age):
    self.color = color
    self.legs = legs
    self.sex = sex
    self.age = age

felix = Cat("ginger", 4, "female", 7)
print(felix.color, felix.legs, felix.sex, felix.age)
print(felix.legs)
print(felix.sex)
print(felix.age)


print()

# In the example above, the __init__ method takes two arguments and assigns them to the object's attributes.
#  The __init__ method is called the class constructor.

# Methods
# =======
# Classes can have other methods defined to add functionality to them.
# Remember, that all methods must have self as their first parameter.
# These methods are accessed using the same dot syntax as attributes.
# Example:

class Dog:
  def __init__(self, name, color):
    self.name = name
    self.color = color

  def bark(self):
    print("Woof!")

fido = Dog("Fido", "brown")
print(fido.name)
fido.bark()

print()

# Classes can also have class attributes, created by assigning variables within the body of the class.
# These can be accessed either from instances of the class, or the class itself.
# Example:

class Dog:
  legs = 4
  def __init__(self, name, color):
    self.name = name
    self.color = color

fido = Dog("Fido", "brown")
print(fido.legs)
print(Dog.legs)

# Class attributes are shared by all instances of the class.

# Classes act as blueprint for object creation, and should be used to model real entities.
# One can define the characters via the attributes, and behavior via the methods of a class.
# Please read the OOP concepts for clarity.
# wiki link : https://en.wikipedia.org/wiki/Object-oriented_programming



# Note that the internal naming for the self parameter must be consistent;
# however, that doesn't necessarily have to be written as self, or as the
# class name, to get a result.
# For example:
print()

class horse:
    def __init__(nag, name, color):
        nag.name = name
        nag.color = color

    def bark(nag):
        print("Neigh!")

myhorse = horse("Trigger", "brown")
print(myhorse.name)
myhorse.bark()

# Substitute self OR horse for nag and the result remains the same.
# This is a useful illustration of what's going on, and fun to play about with
#  - but would get confusing pretty quickly with more complex scripts ;)


# Trying to access an attribute of an instance that isn't defined causes an AttributeError.
# This also applies when you call an undefined method.
# Example:

class Rectangle:
  def __init__(self, width, height, color):
    self.width = width
    self.height = height
    self.color = color

rect = Rectangle(7, 8, "red")
print(rect.color)