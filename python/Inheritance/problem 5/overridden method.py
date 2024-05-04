class A:
    def override_method(self):
        print("Override method from class A")
class B(A):
    def override_method(self):
        print("Override method from class B")
        super().override_method()
class C(B):
    def override_method(self):
        print("Override method from class C")
        super().override_method()
obj_b = B()
obj_c = C()
super(B, obj_b).override_method()  
super(C, obj_c).override_method() 