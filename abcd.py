# # Parent class
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def show_info(self):
#         print(f"Name: {self.name}, Age: {self.age}")
#
#
# # Child class (inherits from Person)
# class Student(Person):
#     def __init__(self, name, age, student_id):
#         # Call constructor of parent class
#         super().__init__(name, age)
#         self.student_id = student_id
#
#     def show_info(self):
#         super().show_info()   # Call parent's method
#         print(f"Student ID: {self.student_id}")
#
#
# # Another child class (inherits from Person)
# class Teacher(Person):
#     def __init__(self, name, age, subject):
#         super().__init__(name, age)
#         self.subject = subject
#
#     def show_info(self):
#         super().show_info()
#         print(f"Subject: {self.subject}")
#
#
# # Example usage
# student1 = Student("Ali", 20, "S123")
# teacher1 = Teacher("Sara", 35, "Mathematics")
#
# print("---- Student Info ----")
# student1.show_info()
#
# print("\n---- Teacher Info ----")
# teacher1.show_info()




from math import pi

# Base Class
class Shape:
    def area(self):
        raise NotImplementedError("Subclass must implement abstract method")

    def perimeter(self):
        raise NotImplementedError("Subclass must implement abstract method")

    def __str__(self):
        return self.__class__.__name__

# Derived Classes
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return pi * self.radius ** 2

    def perimeter(self):
        return 2 * pi * self.radius

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def area(self):
        # Using Heron's Formula
        s = (self.a + self.b + self.c) / 2
        return (s * (s - self.a) * (s - self.b) * (s - self.c)) ** 0.5

    def perimeter(self):
        return self.a + self.b + self.c

# Polymorphism in action
shapes = [
    Circle(5),
    Rectangle(4, 6),
    Triangle(3, 4, 5)
]

for shape in shapes:
    print(f"{shape}: Area = {shape.area():.2f}, Perimeter = {shape.perimeter():.2f}")

print("\n--- Operator Overloading Example ---")

# Polymorphism with operator overloading
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Overload + operator
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    # Overload * operator
    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

    def __str__(self):
        return f"Vector({self.x}, {self.y})"

# Using polymorphism with operators
v1 = Vector(2, 3)
v2 = Vector(4, 5)

print("v1 =", v1)
print("v2 =", v2)
print("v1 + v2 =", v1 + v2)
print("v1 * 3 =", v1 * 3)



class Student:
    def __init__(self, name, age):
        # Private attributes (encapsulated)
        self.__name = name
        self.__age = age

    # Getter method to access private name
    def get_name(self):
        return self.__name

    # Setter method to modify private name
    def set_name(self, name):
        self.__name = name

    # Getter method to access private age
    def get_age(self):
        return self.__age

    # Setter method to modify private age
    def set_age(self, age):
        if age > 0:
            self.__age = age
        else:
            print("Age cannot be negative or zero.")

# Creating object
student = Student("Iqra", 20)

# Accessing data using getter methods
print("Name:", student.get_name())
print("Age:", student.get_age())

# Modifying data using setter methods
student.set_name("Ayesha")
student.set_age(21)

print("\nAfter updating:")
print("Name:", student.get_name())
print("Age:", student.get_age())

