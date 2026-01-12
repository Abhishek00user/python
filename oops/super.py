# super() is a built-in function in Python used to call a method from the parent (base) class.
# it can also Call any overridden method from the parent.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student(Person):
    def __init__(self, name, age, marks):
        super().__init__(name, age)  # call parent constructor
        self.marks = marks

s = Student("Abhishek", 21, 95)
print(s.name, s.age, s.marks)

# calling overridden methods
class Parent:
    def greet(self):
        print("Hello from Parent")

class Child(Parent):
    def greet(self):
        print("Hello from Child")
        super().greet()  # call parent method

c = Child()
c.greet()

# super in multiple inheritance
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
d.show()  #super() follows the MRO: D → B → C → A


# Call: d.show()
# |
# |-- D.show()
# |    print("D")
# |    super().show() --> next in MRO: B
# |
# |-- B.show()
# |    print("B")
# |    super().show() --> next in MRO: C
# |
# |-- C.show()
# |    print("C")
# |    super().show() --> next in MRO: A
# |
# |-- A.show()
#      print("A")
#      super() --> object (ends)
