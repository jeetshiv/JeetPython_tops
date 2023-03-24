"""
print("write")
print("*"*5)
file = open("tops.txt","w")
file.write("file demo example")
file.close()


print("read")
print("*"*5)
file=open("tops.txt","r")
print(file.read())
file.close()


print("read")
print("*"*5)
file=open("tops.txt","a")
file.write("\nappend new")
file=open("tops.txt","r")
print(file.read())
file.close()

"""
file=open("top2.txt","w+")
file.write("read write")
print("file cursor position",file.tell())
file.seek(4)
print(file.read())
file.close()
