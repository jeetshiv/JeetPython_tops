class student:
    def getname(self,n):
        self.name=n
class extramarks:
    def sportsmarks(self,sp):
        self.sm=sp
class result(student,extramarks):
    total=0
    per=0
    def getmarks(self,s1,s2,s3):
        self.phy=s1
        self.chem=s2
        self.maths=s3
        self.total=(self.phy+self.chem+self.maths+self.sm)
        self.per=self.total/4
    def displaydetails(self):
        print("student name",self.name)
        print("total marks",self.total)
        print("percentage",self.per)
res=result()
name=input("enter name")
res.getname(name)
sp=int(input("enter sports marks"))
res.sportsmarks(sp)
p=int(input("input physics marks"))
c=int(input("input chemistry marks"))
m=int(input("input maths marks"))
res.getmarks(p,c,m)
res.displaydetails()
