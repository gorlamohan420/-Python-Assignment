from abc import ABC, abstractmethod
class AbstractClass(ABC):
    def __init__(self, value):
        self.value = value
    @abstractmethod
    def abstract_method(self):
        pass
    def non_abstract_method(self):
        print("This is a non-abstract method")
class ConcreteClass(AbstractClass):
    def abstract_method(self):
        print("This is the implementation of the abstract method")
obj = ConcreteClass(10)
obj.non_abstract_method()
