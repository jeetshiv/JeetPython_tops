""" only 4 digit odd number from 3333 to 3999 sir program """
"""
l=[]

for i in range(3333,3999):
    s = str(i)
    #print(type(s))
    if int(s[0])%2!=0 and int(s[1])%2!=0 and int(s[2])%2!=0 and int(s[3])%2!=0:
        #print(type(s[0]))
        l.append(i)
    
print(l)
"""

def function():
    print("*"*50)
    print("hello")
    print("*"*50)
function()

""" no argument no return value"""
"""
def swpp(a,b):
    print("before swap a=",a,"b=",b)
    a,b=b,a
    print("after swap a=",a,"b=",b)

swpp(2,3)

"""
""" argument with no return value """
"""
def  add(a,b):
    print("a=",a,"b=",b)
    print("addition=",(a+b))

n1=int(input("enter a="))
n2=int(input("enter b="))
add(n1,n2)
"""
"""  with argument with return value """

def  add(a,b):
    print("a=",a,"b=",b)
    return a+b

n1=int(input("enter a="))
n2=int(input("enter b="))
add(n1,n2)

    
def evenodd(n):
    if n%2 == 0:
        print("even")
    else:
        print("odd")

no=add(n1,n2)
print("addition is ",no)
evenodd(no)



