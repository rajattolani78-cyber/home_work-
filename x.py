n = int(input("enter a number to check:- "))
if n > 0:
    print("the number is positive")
    if (n %2) == 0:
        print ("the number is even")
    else:
        print("the number is odd")
elif n ==0:
    print("it is a zero and even too")
elif n<0:
    print("the number is negative")
    if (n %2) == 0:
        print ("the number is even")
    else:
        print("the number is odd")