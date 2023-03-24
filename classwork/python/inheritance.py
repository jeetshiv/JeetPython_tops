"""
single level inheritance
"""
class base:
    fn=""
    ln=""
    def getA(self,a):
        self.base=a
    def putA(self):
        print("base",self.base)
    def accept(self,f,l):
        self.fn=f
        self.ln=l
    def evenodd(self,v):
        self.f=v
        if self.f%2==0:
            print("even:")
        else:
            print("odd")            
class derived(base):
    def getB(self,b):
        self.derived=b
    def putB(self):
        print("derived",self.derived)
    def showdetail(self):
        print("firstname",self.fn)
        print("lastname",self.ln)
n1=int(input("enter base"))
n2=int(input("enter derived"))
fname=input("enter fname")
lname=input("enter lname")
d=int(input("enter"))
obj=derived()
obj.getA(n1)
obj.getB(n2)
obj.accept(fname,lname)
obj.putA()
obj.putB()
obj.showdetail()
obj.evenodd(d)




"""
multilevel inheritance
"""
"""
class A:
    def getA(self,a):
        self.a=a
    def putA(self):
        print("a=",self.a)
class B(A):
    def getB(self,b):
        self.b=b
    def putB(self):
        print("b=",self.b)
class C(B):
    def getC(self,c):
        self.c=c
    def putC(self):
        print("c=",self.c)
n1=int(input("enter"))
n2=int(input("enter"))
n3=int(input("enter"))

obj3=C()
obj3.getA(n1)
obj3.getB(n2)
obj3.getC(n3)
obj3.putA()
obj3.putB()
obj3.putC()
"""
