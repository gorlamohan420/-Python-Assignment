class MyClass:
    static_var = 5
obj = MyClass()
obj.static_var = 2
print(obj.static_var)  
print(MyClass.static_var) 