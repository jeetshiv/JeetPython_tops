import random
data=open("data.txt","w")
for i in range(10):
    num = random.randint(1,999)
    data.write(str(num)+" ")
data.close()


data=open("data.txt","r")
even=open("even.txt","w")
odd=open("odd.txt","w")
s=data.read().split(" ")[:-1]
print(s)

for i in s:
  #  print(type(int(i)))
  if int(i)%2==0:
      even.write(i+" ")
  else:
      odd.write(i+" ")

even.close()
odd.close()
data.close()



print("main list")
print("*"*50)
file=open("data.txt","r")
print(file.read())


print("even list")
print("*"*50)
file=open("even.txt","r")
print(file.read())

print("odd list")
file=open("odd.txt","r")
print("*"*50)
print(file.read())
