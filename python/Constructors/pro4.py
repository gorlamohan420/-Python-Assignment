class Person:
    def __init__(self, name, age):
        self.name = name  
        self.age = age    

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)

person1 = Person("Alice", 30)
person2 = Person("Bob", 25)

print("Person 1:")
person1.display()
print()

print("Person 2:")
person2.display()
