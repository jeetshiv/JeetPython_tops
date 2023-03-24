"""
n=int(input("enter n"))
evensum=0
oddsum=0
for i in range(1,n):
    if i%2==0:
         evensum = evensum+i
    else:
         oddsum = oddsum+i
print("even=",evensum)
print("odd=",oddsum)
"""
for i in range(1,10):
    print("*"*i)

for i in range(1,10):
    print(" "*(9-i),"*"*i)

for i in range(1,10):
    print(" "*(9-i)," *"*i)
for i in range(9,0,-1):
    print(" "*(9-i)," *"*i)

for i in range(9,0,-1):
    print(" "*(9-i)," *"*i)
