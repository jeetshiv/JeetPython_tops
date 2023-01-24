"""
class sample():
    x=0    
    def __init__(self,f):
        self.x=f
        print("default method")
    def demo(self):
        print("function method",self.x)

    def evenodd(self):
        if self.x%2==0:
            print("even")
        else:
            print("odd")
n=int(input("enter number"))
obj  = sample(n)
obj.demo()
obj.evenodd()


class person:
    fn=""
    ln=""
    em=""

    def __init__(self,fn,ln,em):
        self.fname=fn
        self.lname=ln
        self.email=em
    def showdetails(self):
        print("firstname",self.fname)
        print("lastname",self.lname)
        print("email",self.email)

fn=input("enter fname")
ln=input("enter lname")
em=input("enter email")

p=person(fn,ln,em)
p.showdetails()
"""

class BankDemo:
    balance = 0
    
    def checkBalance(self):
        print("Current Balance : ",self.balance)

    def deposit(self,amt):
        self.balance = self.balance + amt
        print("Amount Deposited Successful.")

    def withdraw(self,amt1):
        if amt1<self.balance:
            self.balance = self.balance - amt1
            print("Withdrawal is Successful")
        else:
            print("Insufficient Fund")


p=BankDemo()
p.checkBalance()
amt = int(input("Enter Amount to Deposit : "))
p.deposit(amt)
p.checkBalance()
amt1 = int(input("Enter Amount to Withdraw : "))
p.withdraw(amt1)
p.checkBalance()







