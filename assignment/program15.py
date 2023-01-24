"""
pr:15
 Given a number n, write a python program to make and print the list of Fibonacci series up to n.
Input : n=7 
Hint : first 7 numbers in the series
Expected output : 
First few Fibonacci numbers are 0, 1, 1, 2, 3, 5, 8, 13
"""
d=int(input("enter"))
a=0
b=1
for i in range(d):        
    c=a+b
    print(a)
    a=b
    b=c
