class Parent:
    def __init__(self):
        self.__private_field = "Private Field"
    def __private_method(self):
        print("Private Method")
    def print_private_field(self):
        print("Private Field:", self.__private_field)
    def call_private_method(self):
        self.__private_method()
class Child(Parent):
    def access_private(self):
        print("Trying to access private field from subclass:", self.__private_field)
        print("Trying to call private method from subclass:")
        self.__private_method()

def main():
    obj_parent = Parent()
    obj_parent.print_private_field()
    obj_parent.call_private_method()
    obj_child = Child()
    obj_child.access_private()

if __name__ == "__main__":
    main()
