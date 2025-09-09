# Parent class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_info(self):
        print(f"Name: {self.name}, Age: {self.age}")


# Child class (inherits from Person)
class Student(Person):
    def __init__(self, name, age, student_id):
        # Call constructor of parent class
        super().__init__(name, age)
        self.student_id = student_id

    def show_info(self):
        super().show_info()   # Call parent's method
        print(f"Student ID: {self.student_id}")


# Another child class (inherits from Person)
class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    def show_info(self):
        super().show_info()
        print(f"Subject: {self.subject}")


# Example usage
student1 = Student("Ali", 20, "S123")
teacher1 = Teacher("Sara", 35, "Mathematics")

print("---- Student Info ----")
student1.show_info()

print("\n---- Teacher Info ----")
teacher1.show_info()
