class A:
    def method_A1(self):
        print("Method A1 from class A")
    def override_method(self):
        print("Override method from class A")
class B(A):
    def method_B1(self):
        print("Method B1 from class B")
    def override_method(self):
        print("Override method from class B")
class C(B):
    def method_C1(self):
        print("Method C1 from class C")
    def override_method(self):
        print("Override method from class C")
obj_c = C()
obj_c.method_A1()  
obj_c.method_B1()  
obj_c.method_C1() 
obj_c.override_method()  
