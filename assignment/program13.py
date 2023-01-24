"""
pr13
 Write a Python program to sort a dictionary (ascending /descending) by value.
"""


"""
first method
"""
import operator

d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}

s= dict(sorted(d.items(), key=operator.itemgetter(1)))

print('ascending order : ',s)

s1= dict( sorted(d.items(), key=operator.itemgetter(1),reverse=True))

print('descending order : ',s1)

"""
second method
"""


d={1:2,3:7,5:6}
k=sorted(d.keys())
a=sorted(d.values())
d1=sorted(d.values(),reverse=True)
w=dict(zip(k,a))
q=dict(zip(k,d1))
print("ascending",w)
print("descending",q)
