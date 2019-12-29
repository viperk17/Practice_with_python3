from abc import ABCMeta, abstractmethod


# to make area_print method mandatory for all classes
class Shape(metaclass=ABCMeta):
    @abstractmethod
    def area_print(self):
        return 0


class Rectangle(Shape):
    sides = 4
    type = "Rectangle"

    def __init__(self):
        self.length = 6
        self.breadth = 7

    def area_print(self):
        return self.length * self.breadth


rect1 = Rectangle()
print(rect1.area_print())