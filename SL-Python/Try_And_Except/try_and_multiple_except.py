# try except example with 2 except cases
# remove int() in num lines to provoke TypeError
# you can use multiple except clauses like the example below

try:
    num1 = int(input('Provide num1 ?\n'))
    num2 = int(input ('Provide num2 ?\n'))
    print (num1 / num2)
    print("Done calculation")
except ZeroDivisionError:
    print("An error occurred due to zero division")
except TypeError:
    print ("You didn't type a number")