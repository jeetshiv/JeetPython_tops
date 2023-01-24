

"""
Write a Python function that takes a list and returns a new list with unique elements of the first list.
"""




def fun():
    lis = []
    n=int(input("enter list element"))
    for i in range(n):
        ele=int(input())
        lis.append(ele)
        new_val = set(lis)
    z=list(new_val)
    print("original list",lis)
    print("Unique values:",z)
fun()
