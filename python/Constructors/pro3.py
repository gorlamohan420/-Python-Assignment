#Private:
class MyClass:
    def __init__(self):
        self.__private_attr = 10  #

    def __private_method(self):
        print("This is a private method")

obj = MyClass()

# Protected:
class MyClass:
    def __init__(self):
        self._protected_attr = 20 

    def _protected_method(self):
        print("This is a protected method")

obj = MyClass()

print(obj._protected_attr)  
obj._protected_method()  

#Public:
class MyClass:
    def __init__(self):
        self.public_attr = 30 
    def public_method(self):
        print("This is a public method")
obj = MyClass()
print(obj.public_attr)  
obj.public_method()    


