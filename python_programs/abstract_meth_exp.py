
from abc import abstractmethod, ABC

class Myclass(ABC):
    @abstractmethod
    def mytest(self, a):
        pass

class Hello(Myclass):
    def mytest(self, a):
        print(a)

h = Hello()
print("hello")