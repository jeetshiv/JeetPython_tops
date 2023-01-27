class A:
    def getA(self,a):
        self.a=a
    def putA(self):
        print("a=",self.a)
class B(A):
    def getB(self,b):
        self.b=b
    def putB(self):
        print("B=",self.b)
class C(A):
    def getC(self,c):
        self.c=c
    def putC(self):
        print("c=",self.c)
class D(B,C):
    def getD(self,d):
        self.d=d
    def putD(self):
        print("d=",self.d)
obj=D()
n1=int(input("enter val1"))
n2=int(input("enter val1"))
n3=int(input("enter val1"))
n4=int(input("enter val1"))
obj.getA(n1)
obj.getB(n2)
obj.getC(n3)
obj.getD(n4)
obj.putA()
obj.putB()
obj.putC()
obj.putD()
