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
# class Animal:
#     def __init__(self, name, species):
#         self.name = name
#         self.species = species
#         self.is_alive = True
#
#     def eat(self, food):
#         return f"{self.name} is eating {food}"
#
#     def sleep(self):
#         return f"{self.name} is sleeping"
#
#     def make_sound(self):
#         return f"{self.name} makes a sound"
#
#
# #
# # Child class inherits from Animal
# class Dog(Animal):
#     def __init__(self, name, breed):
#         super().__init__(name, "Canine")  # Call parent constructor
#         self.breed = breed
#         self.loyalty = "High"
#
#     # Override parent method
#     def make_sound(self):
#         return f"{self.name} barks: Woof!"
#
#     # New method specific to Dog
#     def fetch(self, item):
#         return f"{self.name} fetches the {item}"
#
# # Another child class
# class Cat(Animal):
#     def __init__(self, name, indoor=True):
#         super().__init__(name, "Feline")
#         self.indoor = indoor
#         self.independence = "High"
#
#     # Override parent method
#     def make_sound(self):
#         return f"{self.name} meows: Meow!"
#
#     # New method specific to Cat
#     def climb(self, object_name):
#         return f"{self.name} climbs the {object_name}"
#
# # Usage
# dog = Dog("Buddy", "Golden Retriever")
# cat = Cat("Whiskers", True)
#
# # Inherited methods
# print(dog.eat("kibble"))        # Output: Buddy is eating kibble
# print(cat.sleep())              # Output: Whiskers is sleeping
#
# # Overridden methods
# print(dog.make_sound())         # Output: Buddy barks: Woof!
# print(cat.make_sound())         # Output: Whiskers meows: Meow!
#
# # Specific methods
# print(dog.fetch("ball"))        # Output: Buddy fetches the ball
# print(cat.climb("tree"))        # Output: Whiskers climbs the tree
#
# # Inherited attributes
# print(dog.species)              # Output: Canine
# print(cat.is_alive)             # Output: True





# class Shape:
#     def __init__(self, name):
#         self.name = name
#
#     def area(self):
#         pass  # This will be overridden by child classes
#
#     def perimeter(self):
#         pass  # This will be overridden by child classes
#
# class Rectangle(Shape):
#     def __init__(self, width, height):
#         super().__init__("Rectangle")
#         self.width = width
#         self.height = height
#
#     def area(self):
#         return self.width * self.height
#
#     def perimeter(self):
#         return 2 * (self.width + self.height)
#
# class Circle(Shape):
#     def __init__(self, radius):
#         super().__init__("Circle")
#         self.radius = radius
#
#     def area(self):
#         return 3.14159 * self.radius ** 2
#
#     def perimeter(self):
#         return 2 * 3.14159 * self.radius
#
# class Triangle(Shape):
#     def __init__(self, base, height, side1, side2):
#         super().__init__("Triangle")
#         self.base = base
#         self.height = height
#         self.side1 = side1
#         self.side2 = side2
#
#     def area(self):
#         return 0.5 * self.base * self.height
#
#     def perimeter(self):
#         return self.base + self.side1 + self.side2
#
# # Polymorphism in action
# def print_shape_info(shape):
#     """This function works with any shape object"""
#     print(f"Shape: {shape.name}")
#     print(f"Area: {shape.area():.2f}")
#     print(f"Perimeter: {shape.perimeter():.2f}")
#     print("-" * 20)
#
# # Create different shape objects
# rectangle = Rectangle(5, 3)
# circle = Circle(4)
# triangle = Triangle(6, 4, 5, 7)
#
# # List of different shapes
# shapes = [rectangle, circle, triangle]
#
# # Use polymorphism - same function works for all shapes
# for shape in shapes:
#     print_shape_info(shape)
#
# # Output:
# # Shape: Rectangle
# # Area: 15.00
# # Perimeter: 16.00
# # --------------------
# # Shape: Circle
# # Area: 50.27
# # Perimeter: 25.13
# # --------------------
# # Shape: Triangle
# # Area: 12.00
# # Perimeter: 18.00
# # --------------------


# class MathOperations:
#     @staticmethod
#     def add(a, b):
#         return a + b
#
#     @staticmethod
#     def multiply(a, b):
#         return a * b
#
#
# # Using static methods
# print(MathOperations.add(5, 3))  # Output: 8
# print(MathOperations.multiply(4, 2))  # Output: 8



# class Animal:
#     def __init__(self,name,species):
#         self.name=name
#         self.species=species
#         self.alive="true"
#     def eat(self,food):
#         return f"{self.name} is eating {food}"
#     def seep(self):
#         return f"{self.name} is sleeping"
#     def make_sound(self):
#         return f"{self.name} is making sound"
# class Dog(Animal):
#     def __init__(self,name,breed):
#         super(). __init__(name,"canine")
#         self.breed=breed
#         self.loyality="high"
#     def make_sound(self):
#         return f"{self.name} is making sound"
#     def fetch(self,item):
#         return f"{self.name} is fetching{item}"
# class Cat(Animal):
#     def __init__(self,name,indoor="true"):
#         super(). __init__(name,"Feline")
#     def make_sound(self):
#         return f"{self.name} is making sound"
#     def climb(self,item_name):
#         return f"{self.name} is climbing {item_name}"
# dog=Dog("tomy","golden retrival")
# cat=Cat("catoo","true")
# print(dog.make_sound())
# print(cat.make_sound())
# print(dog.eat("kibble"))

class Shape:
    def __init__(self,name):
        self.name=name
    def area(self):
        pass
    def perimeter(self):
        pass
class Rectangle(Shape):
    def __init__(self,width,height):
        super(). __init__("Rectangle")
        self.width=width
        self.height=height
    def area(self):
        return self.width*self.height
    def perimeter(self):
        return 2*(self.width+self.height)
class Circle(Shape):
    def __init__(self,radius):
        super(). __init__("Circle")
        self.radius=radius
    def area(self):
        return 3.14*self.radius**2
    def perimeter(self):
        return 2*3.14*self.radius
class Triangle(Shape):
    def __init__(self,base,height,side1,side2):
        super(). __init__("Triangle")
        self.base=base
        self.height=height
        self.side1=side1
        self.side2=side2
    def area(self):
        return 0.5*self.base*self.height
    def perimeter(self):
        return self.base+self.side1+self.side2
def print_Shape_info(shape):
    print(f"Shape:{shape.name}" )
    print(f"Area:{shape.area()}")
    print(f"Perimeter{shape.perimeter()}")


rectangle=Rectangle(4,5)
triangle=Triangle(5,7,9,4)
circle=Circle(6)
shapes=[rectangle,triangle,circle]
for shape in shapes:
    print_Shape_info(shape)


