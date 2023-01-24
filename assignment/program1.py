"""pr 1 sum of first n positive integers"""

a=int(input("enter positive integers"))
s=0
for i in range(1,a+1):
        s=s+i     
        a=a-1
print(s)
