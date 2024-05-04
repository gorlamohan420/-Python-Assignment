class Superclass:
    def __init__(self, arg=None):
        if arg is None:
            print("Superclass default constructor called")
        else:
            self.arg = arg
            print("Superclass argument constructor called with argument:", self.arg)

class ChildClass(Superclass):
    def __init__(self, arg=None):
        super().__init__()
        
        if arg is not None:
            super().__init__(arg)

child = ChildClass()
print()
child_with_arg = ChildClass("Hello")
