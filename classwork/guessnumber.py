import random

num=random.randint(1,20)


while True:
    n=int(input("enter number between 1 to 20:"))

    if n==num:
        print("Guessed correct number")
        break
    elif n>num:
        print("you guess grater number")
    elif n<num:
        print("you guess less number")
