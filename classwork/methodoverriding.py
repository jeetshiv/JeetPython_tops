"""
class A:
    def show(self,a):
        self.a=a
        print("base class",self.a)

class B(A):
    def show(self,b):
        self.b=b
        print("show from b",self.b)
class C(B):
    def show(self,c):
        self.c=c
        super().show(78)
        print("show from c",self.c)
obj=C()
obj.show(54)
"""

class A:
    def show(self,a):
        self.a=a
        super().show(55)
        print("show from a",self.a)
class B:
    def show(self,b):
        self.b=b
        print("show from b",self.b)
class C(A,B):
    def show(self,c):
        self.c=c
        super().show(78)
        print("show from c",self.c)
obj=C()
obj.show(54)
