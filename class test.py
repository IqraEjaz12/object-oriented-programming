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

# print("welcome to simple calculator")
# number1=float(input("enter the first number"))
# number2=float(input("enter the second number"))
# symbol=input("enter the symbol(+,-,*,/)")
# def add(number1,number2):
#     return number1+number2
# def substract(number1,number2):
#     return number1-number2
# def multiply(number1,number2):
#     return number1*number2
# def divide(number1,number2):
#     return number1/number2
# if symbol=="+":
#     print(f"the sum is :{add(number1,number2)}")
# elif symbol=="-":
#     print(f"the substraction is:{substract(number1,number2)}")
# elif symbol=="*":
#     print(f"the multiplication is:{multiply(number1,number2)}")
# elif symbol=="/":
#     print(f"the division is :{divide(number1,number2)}")
# else:
#     print("invalid input")


class calculator:
    def __init__(self,number1,number2):
        self.number1=number1
        self.number2=number2
    def add(self):
        return self.number1+self.number2
    def substract(self):
        return self.number1-self.number2
    def multiply(self):
        return self.number1*self.number2
    def divide(self):
        return self.number1/self.number2
number1=float(input("enter the first number"))
number2=float(input("enter the second number"))
symbol=input("enter the symbol(+,-,*,/)")
calc=calculator(number1,number2)
if symbol=="+":
    print(f"the sum is :{calc.add()}")
elif symbol=="-":
    print(f"the substraction is:{calc.substract()}")
elif symbol=="*":
    print(f"the multiplication is:{calc.multiply()}")
elif symbol=="/":
    print(f"the division is :{calc.divide()}")
else:
    print("invalid input")


    # Example: Object-Oriented Programming (OOP) in Python

    # Base class
    class Person:
        def __init__(self, name, age):
            self.name = name
            self.age = age

        def show_info(self):
            print(f"Name: {self.name}")
            print(f"Age: {self.age}")


    # Derived class (Inheritance)
    class Student(Person):
        def __init__(self, name, age, student_id, course):
            # Call parent class constructor
            super().__init__(name, age)
            self.student_id = student_id
            self.course = course

        def show_student_info(self):
            self.show_info()  # Call base class method
            print(f"Student ID: {self.student_id}")
            print(f"Course: {self.course}")


    # Another class
    class Teacher(Person):
        def __init__(self, name, age, subject):
            super().__init__(name, age)
            self.subject = subject

        def show_teacher_info(self):
            self.show_info()
            print(f"Subject: {self.subject}")


    # Create objects
    student1 = Student("Iqra Ejaz", 20, "2024-AG-6561", "BS IT")
    teacher1 = Teacher("Sir Ali", 35, "Programming")

    # Display information
    print("=== Student Information ===")
    student1.show_student_info()

    print("\n=== Teacher Information ===")
    teacher1.show_teacher_info()
