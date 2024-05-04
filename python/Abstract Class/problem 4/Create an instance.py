from abc import ABC, abstractmethod
class AbstractClass(ABC):
    @abstractmethod
    def abstract_method(self):
        pass
    def non_abstract_method(self):
        print("Non-abstract method in AbstractClass")
class ConcreteClass(AbstractClass):
    def abstract_method(self):
        print("Implementation of abstract method in ConcreteClass")
    def call_non_abstract_method(self):
        self.non_abstract_method()
class_instance = ConcreteClass()
class_instance.call_non_abstract_method()