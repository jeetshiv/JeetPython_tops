"""
pr:4 Write a Python program to get a single string from two given strings, separated by a space and swap the first 
two characters of each string. 
"""

str1 = input("Please Enter First String : ")
str2 =input("Please Enter Second String : ")

x=str1[0:2]

str1=str1.replace(str1[0:2],str2[0:2])

str2=str2.replace(str2[0:2],x)

print("Your first string has become :- ",str1)
print("Your second string has become :- ",str2)
