"""
pr6
 Write a Python program to find the first appearance of the substring 'not' and 'poor' from a given string, if 
'not' follows the 'poor', replace the whole 'not'...'poor' substring with 'good'. 
Return the resulting string
"""


c=input("enter string")
if(c.find("not poor",-1,10)):
        t=c.replace("not poor","good good",1)
print(t)
