# Inheritance is a mechanism where a class acquires the properties and behaviors of another class, enabling code reuse and hierarchical relationships.

class Vehicle:
    def move(self):
        print("Vehicle is moving")

class Car(Vehicle):
    def drive(self):
        print("Car is driving")

c = Car()
c.move()
c.drive()



# super use
class Animal:
    def sound(self):
        print("Animal sound")

class Dog(Animal):
    def sound(self):
        super().sound()
        print("Dog barks")

d = Dog() # Animal sound
d.sound() # Dog barks



# inheriting constructor
class Parent:
    def __init__(self):
        print("Parent constructor")

class Child(Parent):
    def __init__(self):
        super().__init__()  # if not called then parent initialization skipped
        print("Child constructor")

c = Child()  # parent called first and then child


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")

class Student(Person):
    def __init__(self, name, age, marks):
        super().__init__(name, age)  # inheriting parent constructor and no need to use self here in args
        self.marks = marks

    def show_marks(self):
        print(f"Marks: {self.marks}")

s = Student("Abhishek", 21, 95)
s.display()     # inherited method
s.show_marks()  # child method


# multiple inheritance
class Father:
    def skills(self):
        print("Gardening")

class Mother:
    def skills(self):
        print("Cooking")

class Child(Mother , Father):
    pass

c = Child()
c.skills()  # In multiple inheritance, Python uses MRO (Method Resolution Order) and takes first parent (Mother)

# diamond problem 
# by using super , Python ensures that each class is called only once in the diamond hierarchy.
# super follows parent , not immediate parent
class A:
    def show(self):
        print("A")

class B(A):
    def show(self):
        print("B")
        super().show()

class C(A):
    def show(self):
        print("C")
        super().show()

class D(B, C):
    def show(self):
        print("D")
        super().show()

d = D()
d.show()

print(D.mro())

# FLOW
# D.show() → prints D

# super() → goes to next in MRO → B

# B.show() → prints B

# super() → goes to next in MRO → C

# C.show() → prints C

# super() → goes to next in MRO → A

# A.show() → prints A

# super() → goes to object

# Stops

# MRO obeys 3 guarantees:

# No duplicates
# → Each class appears once
# Child before parent
# → D before B, C; B, C before A
# Left-to-right priority
# → B before C in D(B, C)
# These rules force a single, conflict-free path.