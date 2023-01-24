"""
pr7:
Program to find Greatest Common Divisor of two numbers.
For example, the GCD of 20 and 28 is 4 and GCD of 98 and 56 is 14

"""


"""using math libriary """

import math
  
# prints 12
print("The gcd of 20 and 28 is : ", end="")
print(math.gcd(20, 28))

""" without math libriary """

num1 = 20
num2 = 28
a = num1
b = num2

while num1 != num2:
    if num1 > num2:
        num1 -= num2
    else:
        num2 -= num1

print("GCD of", a, "and", b, "is", num1)
