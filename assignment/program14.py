"""
pr14
Write a Python program to find the highest 3 values in a dictionary.

"""

"""first method"""

from collections import Counter
my_dict = {'t': 3, 'u': 4, 't': 6, 'o': 5, 'r': 21}
print("Dictionary=",my_dict)
k = Counter(my_dict)
high = k.most_common(3)
print("Dictionary with 3 highest values:")
print("Keys: Values")
for i in high:
   print(i[0]," :",i[1]," ")


""" second method"""


d = {'a':1,'b':5,'c':7,'d':8,'e':9}
d1=sorted(d.values(),reverse=True)
print("dictionary=",d)
print("highest 3 values in dictionary")
for x in list(d1)[0:3]:
    print(x)
