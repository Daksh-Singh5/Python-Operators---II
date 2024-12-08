num1=float(input("what is your first number "))
num2=float(input("what is your second number "))
num3=float(input("what is your third number "))

if num1>num2 and num1>num3:
    print(num1,"is the greatest number")
elif num2>num1 and num2>num3:
    print(num2,"is the greatest number")
elif num3>num1 and num3>num2:
    print(num3,"is the greatest number")
elif num1==num2==num3:
    print("all numbers are equal")
elif num1==num2:
    print(num1,num2,"are equal")
elif num3==num2:
    print(num3,num2,"are equal")
elif num1==num3:
    print(num1,num3,"are equal")
