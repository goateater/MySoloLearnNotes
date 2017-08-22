
#To play with modules
#====================
#	1. To import multiple modules we can use import math, random, sys

#	2. To import only some useful functions of a module, we can use the code as from math import sqrt

#	3. We can also give some alias name to the particular function after import statement from math import sqrt as square_root

#	4. We can also give alias names for different functions with in a module using commas.

#	from math import sqrt as square_root, cos as cosine, tan as tangent
#	print square_root(49)
#	>>>7.0
#	print cosine(0)
#	>>>1
#	print tan(45)
#	>>>1

#	5. We can print the list of all functions within a module using the line of code
#	import math

#	print dir(math)
#	>>>['__doc__', '__name__', '__package__', 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'ceil', 'copysign', 'cos', 'cosh', 'degrees', 'e', 'erf', 'erfc', 'exp', 'expm1', 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'hypot', 'isinf', 'isnan', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'modf', 'pi', 'pow', 'radians', 'si


#Modules
#=======
#You can import a module or object under a different name using the as keyword.
#This is mainly used when a module or object has a long or confusing name.
#For example:


from math import sqrt as square_root

print(square_root(100))