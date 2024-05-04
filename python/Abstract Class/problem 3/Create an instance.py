from abc import ABC, abstractmethod
class AbstractClass(ABC):
    @abstractmethod
    def abstract_method(self):
        pass
class ConcreteClass(AbstractClass):
    def abstract_method(self):
        print("Implementation of abstract method in ConcreteClass")
    def call_abstract_method(self):
        self.abstract_method() 
class_instance = ConcreteClass()
class_instance.call_abstract_method()
