"""
pr:5
Write a Python program to add 'ing' at the end of a given string (length should be at least 3). 
If the given string already ends with 'ing' then add 'ly' instead If the string length of the given 
string is less than 3, leave it unchanged 

"""
c=input("enter string")
if len(c)>3:
    if c.endswith("ing"):
        t=c+"ly"
        print(t)
    else:
        t=c+"ing"
        print(t)
else:
    print(c)
