class MyClass:
    def __init__(self):
        self.field = 10

try:
    obj = MyClass()
    value = obj.non_existent_field  
except AttributeError:
    print("Error: No such field!")
