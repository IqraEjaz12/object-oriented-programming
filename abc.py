# stuname = "saira"
# stuage = 21
# sturoll = 21212
#
#
# stuname = "Iqra"
# stuage = 20
# sturoll = 45645
#
# def feesubmit(stuname):
#     print("Submitting fee")
#
#
# class Student:
#
#
#     def __init__(self, name , age, rollnum):
#             self.name = name
#             self.age = age
#             self.rollnum = rollnum
#
#
#
#
#
#     def submitFee(self):
#         print("Can submit fee")
#
#
#
# ob1 = Student("saira", 21, 3445)
# print(ob1.name)
#
# ob2 = Student("iqra", 22,465)
# print(ob2.name)
#
# ob3= Student("Hmna",25,345)
# print(ob3.name)
#
#
#
#
#
# class Student:
#     def __init__(self,name,age,roll_no):
#         self.name=name
#         self.age=age
#         self.roll_no=roll_no
#
#     def fee_submit(self):
#         print("Student is paying his/her fee")
# ob1=Student("iqra",21,235)
#
#
# print(ob1.name)
# ob1.fee_submit()
#
#
#
# class Student:
#
#     def __init__(self):
#         print("This is constructor function")
#
#
#
#
# saira = Student()
#




# class Car:
#     _color = "Blue"
#     __engine = "Combussion engine"
#
#
#     #Default contructor
#     def __init__(self):
#         print("This is my default constructor")
#
#
#     def __init__(self, name, model, wheel, companyName):
#         self.name = name
#         self.model = model
#         self.wheel = wheel
#         self.companyName = companyName
#         self.__engine_style = "BAcd"
#     # #
#     # #
#     def __need_oil(self):
#         print("I need oil to run")
#     def forwardCar(self):
#         print("Car is about to forward")
#         print(self.__engine_style)
#         self.__need_oil()
#
#     def changeEngineType(self, engineName):
#         self.engine = engineName
#
#     def changemodel(self,modelName):
#         self.model=modelName
#     @staticmethod
#     def printFunction():
#         print("This is a static method")
#
#
#
#
# ob = Car("BMW", "ABD!@", 4,"BMW Corporation")
# ob._color = "Green"
# print(ob._color)
#

# Parent class (Base class)
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.is_alive = True

    def eat(self, food):
        return f"{self.name} is eating {food}"

    def sleep(self):
        return f"{self.name} is sleeping"

    def make_sound(self):
        return f"{self.name} makes a sound"


#
# Child class inherits from Animal
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, "Canine")  # Call parent constructor
        self.breed = breed
        self.loyalty = "High"

    # Override parent method
    def make_sound(self):
        return f"{self.name} barks: Woof!"

    # New method specific to Dog
    def fetch(self, item):
        return f"{self.name} fetches the {item}"

# Another child class
class Cat(Animal):
    def __init__(self, name, indoor=True):
        super().__init__(name, "Feline")
        self.indoor = indoor
        self.independence = "High"

    # Override parent method
    def make_sound(self):
        return f"{self.name} meows: Meow!"

    # New method specific to Cat
    def climb(self, object_name):
        return f"{self.name} climbs the {object_name}"

# Usage
dog = Dog("Buddy", "Golden Retriever")
cat = Cat("Whiskers", True)

# Inherited methods
print(dog.eat("kibble"))        # Output: Buddy is eating kibble
print(cat.sleep())              # Output: Whiskers is sleeping

# Overridden methods
print(dog.make_sound())         # Output: Buddy barks: Woof!
print(cat.make_sound())         # Output: Whiskers meows: Meow!

# Specific methods
print(dog.fetch("ball"))        # Output: Buddy fetches the ball
print(cat.climb("tree"))        # Output: Whiskers climbs the tree

# Inherited attributes
print(dog.species)              # Output: Canine
print(cat.is_alive)             # Output: True