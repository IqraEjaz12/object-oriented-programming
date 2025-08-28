from abc import ABC, abstractmethod

# Abstract class
class Shape(ABC):

    @abstractmethod
    def area(self):   # abstract method
        pass


# Subclass 1
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):   # must implement area
        return self.width * self.height


# Subclass 2
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):   # must implement area
        return 3.14 * (self.radius ** 2)


# Using the classes
shapes = [Rectangle(5, 3), Circle(4)]

for shape in shapes:
    print(f"{shape.__class__.__name__} area: {shape.area()}")
