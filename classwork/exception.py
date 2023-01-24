"""
try:
    
    a=int(input("enter a"))
    b=int(input("enter b"))
    div=a/b
    print(div)
except Exception:
    print("exception caught")

except ZeroDivisionError:
    print("exception caught")
except ValueError:
    print("exception caught")
    
"""
while True:
    try:
      a=input("enter value")
      n=int(a)
      break
    except Exception:
        print("invalid input")
    finally:
        print("finally called")
print("bye")
