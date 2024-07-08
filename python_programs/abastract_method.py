from abc import ABC, abstractmethod
class polygon(ABC):


    @abstractmethod
    def no_of_sides(self):
        pass

class Triangle(polygon):
    def __init__(self):
        pass
    def no_of_sides(self):
        print("i have three sides")

class reactangle(polygon):
    def __init__ (self):
        pass
    def no_of_sides(self):
        print("i have foure sides")
obj1 = Triangle()
obj2 = reactangle()
obj1.no_of_sides()
obj2.no_of_sides()


