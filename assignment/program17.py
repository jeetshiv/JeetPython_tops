"""
Write a python program using function to find the sum of odd series and even series
Odd series: 12/ 1! + 32/ 3! + 52/ 5!+……n 
Even series: 22/ 2! + 42/ 4! + 62/ 6!+……n

"""

import math
def odd():
    s=0
    f=1
    i=12
    e=1
    n=int(input("enter"))

    for j in range(1,n+1):
    
        s=s+i/math.factorial(e)
        i=i+20
        e=e+2
    print("odd series=",s)
odd()

def even():
    s=0
    f=1
    i=22
    e=2
    n=int(input("enter"))

    for k in range(1,n+1):
    
        s=s+i/math.factorial(e)
        i=i+20
        e=e+2
    print("even series=",s)
even()


