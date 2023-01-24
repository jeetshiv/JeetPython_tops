l2=[100,1.1,2.2,200,"py","el",400,500,400.22]
print(l2[:])
print(l2[1:11])
print(l2[5:7])
print(l2[3:])
print(l2[:10])
print(l2[1:11:2])



print(l2[-1:-11:-1])
print(l2[-3:-2])
print(l2[-3:])
print(l2[:-7])


""" list as stack"""


l3=[]
l3.append(100)
print(l3)
l3.append(200)
print(l3)
l3.append("tops")
print(l3)
l3.pop()
print(l3)


""" list as queue """
from _collections import deque
l=deque([])
l.append(10)
print(l)
l.append(20)
print(l)
print(list(l))
l.popleft()
print(list(l))
