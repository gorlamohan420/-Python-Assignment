class A:
    def method_A(self):
        print("Method from class A")
class B(A):
    def method_B(self):
        print("Method from class B")
class C(B):
    def method_C(self):
        print("Method from class C")
obj_c = C()
obj_c.method_A()  
obj_c.method_B() 
obj_c.method_C() 
