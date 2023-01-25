"""
pr:20
Problem Statement : Password Generator
Make a program to generate a strong password using the input given by the user. To generate a password,
randomly take some words from the user input and then include numbers, special characters and capital
letters to generate the password. Also, keep a check that password length is more than 8 characters.
Note: Include Exception handling wherever required. Also, make a ‘User’ class and store the details like user
id, name and password of each user as a tuple
"""

import random
class User:
    def getA(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
        
        if len(self.c) < 8:
            print("password more then 8 character")
        elif self.c.isalpha():
            print("Include digit and special characters")
        elif self.c.isdigit():
            print("Include characters and special characters")
        elif self.c.isalnum():
            print("Include special character")
        elif self.c.islower():
            print("Include upper case digit")
        elif self.c.isupper():
            print("Include lower case digit")
        else:
                tup=()
                t=list(tup)
                for i in range(1):
                    sc=random.randint(32,47)
                    tc=chr(sc)
                    z=self.c+tc
                    #tup.include(self.a,self.b,z)
                    t.append('idno=')
                    t.append(self.a)
                    t.append('name=')
                    t.append(self.b)
                    t.append('password=')
                    t.append(z)
                    print(t)

n1=input("enter Id")
n2=input("enter Name")
n3=input("enter Password")
obj= User()
obj.getA(n1,n2,n3)
