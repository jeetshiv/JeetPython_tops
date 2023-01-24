l=[1,2,3,"python",2.2,2.3,True,False,0,2,3,1]
print(l)

l1=l.copy()
l1.append(100)
print(l1)


l2=l.copy()
l2.append(200)
print(l2)

l1.pop()
print(l1)

print(l1.count(1))
print(l1.count(0))



l3=[100,200,300]
l.extend(l3)
print(l)

l3.insert(0,"tops")
l3.insert(3,"top")
print(l3)


l3.reverse()
print(l3)
