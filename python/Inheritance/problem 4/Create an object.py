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
class Main:
    def main(self):
        obj_a = A()
        obj_b = B()
        obj_c = C()
        obj_a.method_A1()
        obj_a.override_method()
        obj_b.method_B1()
        obj_b.override_method()
        obj_c.method_C1()
        obj_c.override_method()

if __name__ == "__main__":
    main_instance = Main()
    main_instance.main()
