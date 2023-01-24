def grttwo(a,b):
    if a>b:
        print("a is Greater")
    else:
        print("b is greater")

def grtthree(a,b,c):
    if a>b:
        if a>c:
            print("a  is great")
        else:
            print("c is great")
    if b>a:
        if b>c:
            print("b is great")
        else:
            print("c is great")

def evenodd(a):
    if a%2==0:
        print("even number")
    else:
        print("odd number")


def check(n): 
    for i in range(2,n):
        if n%i==0:
            print("not prime")
            break
    else:
            print("prime")
check(9)        

def fibo():
        
   d=int(input("enter"))
   a=0
   b=1
   for i in range(d):
        
        c=a+b
        print(a)
        a=b
        b=c

