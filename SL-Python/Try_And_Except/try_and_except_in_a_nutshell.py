t_and_e = """
There are three types of errors:

1. Syntax Errors
Happen when you write improper Python language. A program with even a single syntax error won't run.

2. Runtime Errors
Happen while the program is running.
The program will run until the line of code with errors and then terminate the program. 
This is called crashing. Traceback is also displayed.

3. Semantic Errors
Don't crash a program. They are errors in terms of context and meaning.
Only the programmer can notice this.

so..

print(Runtime Errors == Exception)
True

Runtime Error is the same with Exception and that means exception is just a sort of error!

Exceptions
=========
Different exceptions are raised for different reasons. 
Common exceptions:
ImportError: an import fails;
IndexError: a list is indexed with an out-of-range number;
NameError: an unknown variable is used;
SyntaxError: the code can't be parsed properly; 
TypeError: a function is called on a value of an inappropriate type;
ValueError: a function is called on a value of the correct type, but with an inappropriate value.

"""

print(t_and_e)