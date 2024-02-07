# Written by Tiago Perez

import math_operations

result1 = math_operations.add_numbers(5, 3)
print("Result 1:", result1)

from math_operations import add_numbers

result2 = add_numbers(10, 7)
print("Result 2:", result2)

from math_operations import add_numbers as fn

result3 = fn(8, 2)
print("Result 3:", result3)

import math_operations as mn

result4 = mn.add_numbers(15, 6)
print("Result 4:", result4)

from math_operations import *

result5 = add_numbers(20, 4)
print("Result 5:", result5)
