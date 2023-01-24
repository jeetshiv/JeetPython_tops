"""pr 1 sum of first n positive integers"""
"""
a=int(input("enter positive integers"))
s=0
for i in range(1,a+1):
        s=s+i     
        a=a-1
print(s)
"""
""" pr 2 """
"""
s = "hello world"
print(s.count('hello'))
"""

""" pr3 """
"""
str=input("enter sentence")
#str = "To change the overall look your document. To change the look available in the gallery"
c = dict()
txt = str.split(" ")
for t in txt:
	if t in c:
		c[t] += 1
	else:
		c[t] = 1
print(c)

"""
""" pr 4"""
"""
str1 = input("Please Enter First String : ")
str2 =input("Please Enter Second String : ")

x=str1[0:2]

str1=str1.replace(str1[0:2],str2[0:2])

str2=str2.replace(str2[0:2],x)

print("Your first string has become :- ",str1)
print("Your second string has become :- ",str2)
"""
"""

"""

"""
pr 5
"""
"""
c=input("enter string")
if c.endswith("ing"):
        t=c+"ly"
        print(t)
else:
        t=c+"ing"
        print(t)
"""
"""
pr 6
"""
"""
c=input("enter string")
if(c.find("not poor",-1,10)):
        t=c.replace("not poor","good good",1)
print(t)
"""
"""pr 7 gcd of two number """
"""using math libriary """
"""
import math
  
# prints 12
print("The gcd of 20 and 28 is : ", end="")
print(math.gcd(20, 28))
"""
""" without math libriary """
"""
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
"""
"""pr 8 """
"""
list = [[1,5,7,], [2, 3, 4], [3, 6, 9], [4, 8, 12]] 
check_list = [2,3,4]
if check_list in list: 
	print("List is present") 
else: 
	print("List is not present") 
"""


""" pr9 """

"""
li = [] 
n = int(input("Enter the number of elements: "))
for i in range(1, n+1): 
    elem = int(input("Enter the elements: ")) 
    li.append(elem) 
li.sort() 

print("The sorted list: ", li) 
print("The second smallest value of this list: ",li[1])
"""
""" pr10 """
"""
new_lis = [14,25,87,14,78,25,25]

new_val = set(new_lis)
z=list(new_val)

print("Unique values:",z)
"""
"""pr11"""
"""
l = [(1,2), (3,4), (8,9)]
print(list(zip(*l)))
"""
""" pr 12"""
"""
tuples = [('Key 1', 1), ('Key 2', 2), ('Key 3', 3), ('Key 4', 4), ('Key 5', 5)]
result = dict(tuples)
print(result)
"""
"""pr13"""
"""

import operator

d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}

s= sorted(d.items(), key=operator.itemgetter(1))

print('ascending order : ',s)

s1= dict( sorted(d.items(), key=operator.itemgetter(1),reverse=True))

print('descending order : ',s1)

"""
""" pr14 """
"""
from collections import Counter
# Initial Dictionary
my_dict = {'t': 3, 'u': 4, 't': 6, 'o': 5, 'r': 21}
k = Counter(my_dict)
# Finding 3 highest values
high = k.most_common(3)
print("Dictionary with 3 highest values:")
print("Keys: Values")
for i in high:
   print(i[0]," :",i[1]," ")
"""

""" pr 15 fibonacci"""
"""
   d=int(input("enter"))
   a=0
   b=1
   for i in range(d):
        
        c=a+b
        print(a)
        a=b
        b=c
"""



