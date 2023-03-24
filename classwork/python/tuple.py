t=(100,200,300,True,False,"tops",[100,200],1.1,2.2)
print(t)
print(t.count(0))
print(t[6])
t[6].append(300)
print(t[6])
print(len(t))
print(t.index(True))

for i in t:
    print(i)

print(200 in t)


"""
tuple slicing
"""
print("slicing")
t2=(200,300,70,2,[200,300],2.2,"top",True,3,5)
print(t2[:])
print(t2[2:])
print(t2[:5])
print(t2[2:5])
print(t2[2:7:2])


print(t2[-4:])
print(t2[:-2])
print(t2[-8:-2])
print(t2[-2:-10:-4])


"""
"""
l=[]
for i in range(1000,2001):
    if i % 7==0 and i % 5 !=0:    
        l.append(i)
print(l)
