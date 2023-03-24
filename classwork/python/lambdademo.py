"""
    Lambda function:

    A function without the name is called a lambda function
    lambda function is called as anonymous function.
    lambda  function can take multiple arguments

    in lambda function we can not write conditional statements
    if/else loops,etc

      - lambda function only takes an expression          
        -lambda function contains by default return keyword.
        syntax:
                lambda arg-lists: expression
    e.g  lambda x : print(x) 
"""
"""
add = lambda a,b:a+b
#print(add)
#print(add(10))
print(add(50,50))
"""

#UDF
#def add(a,b):
#   return a+b

add = lambda a,b : a+b
print(add(50,10))
