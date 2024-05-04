class MyClass:
    def __init__(self):
        self.public_field = "Public Field"
    def public_method(self):
        print("Public Method")
class OtherClass:
    def access_public(self, obj):
        print("Accessing public field from another class in the same package:", obj.public_field)
        obj.public_method()
obj = MyClass()
other_obj = OtherClass()
other_obj.access_public(obj)
