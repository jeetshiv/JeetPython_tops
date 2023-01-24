print("student mark")
print("enter physics marks")
n1=int(input("enter physics marks"))
n2=int(input("enter chemistry marks"))
n3=int(input("enter maths marks"))
tot=n1+n2+n3
per=tot/3
print("phy=",n1,"chem=",n2,"maths=",n3,"tot=",tot,"per=",per)
if(per >70):
  print("distinction")
elif(per>=60):
  print("A grade")
elif(per>=50):
  print("B grade")
elif(per>=35):
  print("C grade")
else:
  print("fail")
