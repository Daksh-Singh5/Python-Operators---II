num1=float(input("what is your height "))
num2=float(input("what is your weight "))
BMI = num2/(num1**2)
print(BMI)
if BMI <18.5:
    print("you are Underweight")
elif BMI >18.5 and BMI<24.9:
    print("you are Normal")
elif BMI >25 and BMI<29.9:
    print("you are overweight")
elif BMI >30 and BMI<34.9:
    print("you are obese")
elif BMI >35 and BMI<39.9:
    print("you are severely obese")
elif BMI >40:
    print("you are Morbidly obese")
