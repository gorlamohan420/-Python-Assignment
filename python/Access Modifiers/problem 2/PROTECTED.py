class Parent:
    def __init__(self):
        self._protected_field = "Protected Field"
    def _protected_method(self):
        print("Protected Method")
class OtherClass:
    def access_protected(self, obj):
        print("Accessing protected field from another class in the same package:", obj._protected_field)
        obj._protected_method()
class Child(Parent):
    def access_protected(self):
        print("Accessing protected field from child class in a different package:", self._protected_field)
        self._protected_method()
