"""

 Counting the frequencies in a list using a dictionary in Python.
Input : [1, 1, 1, 5, 5, 3, 1, 3, 3, 1,4, 4, 4, 2, 2, 2, 2]
Expected output : 1 : 5 , 2 : 4 , 3 : 3 , 4 : 3 , 5 : 2

"""
d={}
l=["a","b","d","d"]
for i in l:
    if i in d:
        d[i]=d[i]+1
    else:
        d[i]=1
print(d)
