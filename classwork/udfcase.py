import udf
while True:
    print("1 for two number add")
    print("2 for three number add")
    print("3 for even odd")
    print("4 for prime")
    print("5 for fibonanci")
    print("6 for exit")

    choice=int(input("enter choice"))

    if choice==1:
      a=int(input("enter first number"))
      b=int(input("enter second number"))
      udf.grttwo(a,b)
    elif choice==2:
      a=int(input("enter first number"))
      b=int(input("enter second number"))
      c=int(input("enter third number"))
      udf.grtthree(a,b,c)

    elif choice==3:
      a=int(input("enter number"))
      udf.evenodd(a)

    elif choice==4:
      a=int(input("enter number"))
      udf.check(a)

    elif choice==5:
      udf.fibo()
    else:
        break
      
