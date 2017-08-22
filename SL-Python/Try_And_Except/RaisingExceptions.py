# Raising Exceptions
# You can raise exceptions by using the raise statement.
# This is mainly used to test out your code and to raise exceptions when user input is incorrect

try:
       x = int(input("Enter integer: "))
       if not isinstance(x,int):
            raise ValueError
       print("x * 5 = ", x*5)
except ValueError:
       print(" the hell did you enter")

# Now only integers will trigger the code to print a value times 5

# In except blocks, the raise statement can be used without arguments to re-raise whatever exception occurred.
# For example:

try:
   num = 5 / 0
except:
   print("An error occurred")
   raise

# Result:
# >>> An error occurred
# >>> ZeroDivisionError: division by zero

# You can use raise outside of a try and except clause as well

print(1)
raise ValueError
print(2)
