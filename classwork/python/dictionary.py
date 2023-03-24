d={1:'kanak',2:'anam',3:'ved',4:'dfs'}
print(d)
print(d[1])

d1=d.copy()
print(d1)
print(d.get(5))
print(d.get(2))
print(d.keys())
print(d.values())
print(d.items())


d1.pop(4)
print(d1)
print(d1.pop(3))
print(d1.popitem())
print(d1)



d2={'a':1,'b':2,'c':3}
d1.update(d2)
print(d1)


d[1]='lalita'
print(d)
d[2]='jayant'
print(d)
d[2]='jay'
print(d)
d[5]='ankit'
d[6]='mohit'
print(d)

"""
for i in d.values():
    print(d)
"""
"""
d3={}
n=int(input("enter"))
for i in range(1,n+1):
    d3[i]=i*i
print(d3)
"""
"""
2000 to 3000 all 4 digit no even print in list
"""

lst=[]
for i in range(2000,3000+1):
    l1=i//10
    l2=l1//10
    l3=l2//10
    if  (i%10==2 or i%10==0 or i%10==4 or i%10==6 or i%10==8) and (l1%10==0 or l1%10==2 or l1%10==4 or l1%10==6 or l1%10==8) and (l2%10==0 or l2%10==2 or l2%10==4 or l2%10==6 or l2%10==8) and (l3%10==0 or l3%10==2 or l3%10==4 or l3%10==6 or l3%10==8):
        lst.append(i)
print(lst)
    
    
        
        
    


