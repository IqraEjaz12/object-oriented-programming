# print("welcome to simple calculator")
# number1=float(input("enter the first number"))
# number2=float(input("enter the second number"))
# symbol=input("enter the symbol(+,-,*,/)")
# if symbol=="+":
#     sum=number1+number2
#     print(f"the sum is :{sum}")
# elif symbol=="-":
#     substraction=number1-number2
#     print(f"the substraction is:{substraction}")
# elif symbol=="*":
#     multiplication=number1*number2
#     print(f"the multiplication is:{multiplication}")
# elif symbol=="/":
#     division=number1/number2
#     print(f"the division is :{division}")
# else:
#     print("invalid input")

print("welcome to simple calculator")
number1=float(input("enter the first number"))
number2=float(input("enter the second number"))
symbol=input("enter the symbol(+,-,*,/)")
def add(number1,number2):
    return number1+number2
def substract(number1,number2):
    return number1-number2
def multiply(number1,number2):
    return number1*number2
def divide(number1,number2):
    return number1/number2
if symbol=="+":
    print(f"the sum is :{add(number1,number2)}")
elif symbol=="-":
    print(f"the substraction is:{substract(number1,number2)}")
elif symbol=="*":
    print(f"the multiplication is:{multiply(number1,number2)}")
elif symbol=="/":
    print(f"the division is :{divide(number1,number2)}")
else:
    print("invalid input")