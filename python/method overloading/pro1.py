class MyClass:
    def same_name_method(self, x):
        print("Method with one parameter called")
        print("Value of x:", x)

    def same_name_method(self, x, y):
        print("Method with two parameters called")
        print("Value of x:", x)
        print("Value of y:", y)

obj = MyClass()
obj.same_name_method(10)
print()
obj.same_name_method(10, 20)
