class Class1:
    def __init__(self, name):
        self.name = name

    def display_name(self):
        print("Name from Class1:", self.name)
class Class2:
    def __init__(self, value):
        self.value = value

    def display_value(self):
        print("Value from Class2:", self.value)
from my_package.class1 import Class1
from my_package.class2 import Class2

obj1 = Class1("Mohan")
obj2 = Class2(42)

obj1.display_name()
obj2.display_value()
