class A:
    def __init__(self):
        self.data = "Data from class A"
    def display_data(self):
        print("Data:", self.data)
class B(A):
    def __init__(self):
        super().__init__()
        self.data = "Data from class B"
    def display_data(self):
        print("Data:", self.data)
class C(B):
    def __init__(self):
        super().__init__()
        self.data = "Data from class C"
    def display_data(self):
        print("Data:", self.data)
obj_B = B()
obj_C = C()
print("Data from class A using superclass reference:", super(B, obj_B).data)  
print("Data from class A using superclass reference:", super(C, obj_C).data)  
