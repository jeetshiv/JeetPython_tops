class length:
    def getval(self,l):
        self.l=l
class square(length):
    def sqr(self):
        return self.l*self.l
class cube(length):
    def cub(self):
        return self.l*self.l*self.l

sq=square()
n1=int(input("enter no for square"))

sq.getval(n1)
val=sq.sqr()
print("square is=",val)

c=cube()
n2=int(input("enter for cube"))
c.getval(n2)
val2=c.cub()
print("cube is",val2)
