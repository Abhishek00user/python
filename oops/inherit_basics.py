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



# super use - The super() function in Python is used to call methods from a parent class (also called the superclass) from within a child class (or subclass)
class Animal:
    def sound(self):
        print("Animal sound")

class Dog(Animal):
    def sound(self):
        super().sound()  # Calls the method from the parent class (Animal)
        print("Dog barks")

d = Dog() # creating an instance of the dog
d.sound() # Dog barks

# When d.sound() is called on the Dog object d:
# First, the sound() method from the parent class Animal is called using super().sound(), printing "Animal sound".
# Then, the sound() method in the Dog class continues to execute, printing "Dog barks".

# inheriting constructor
class Parent:
    def __init__(self):
        print("Parent constructor")

class Child(Parent):
    def __init__(self):
        super().__init__()  #calling init method of the parent class .This is crucial because it ensures that the Parent class is properly initialized before the Child class does its own initialization. if not used then parent initialization skipped
        print("Child constructor")

c = Child()  # parent called first and then child
# if the parent class needs to perform some essential setup (like initializing instance variables) that the child class object would relies on , then it is important to use super 

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")

class Student(Person):
    def __init__(self, name, age, marks):
        super().__init__(name, age)  #  no need to use self here in args
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
c.skills()  # In multiple inheritance, Python uses MRO (Method Resolution Order) and takes first parent (Mother) , so here cooking will be done


# code for understanding the MRO order
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

# MRO of this -> D → B → C → A → object . Because all classes use super(), Python follows the MRO . so each method runs only once
d = D()
d.show()  # ouput is D B C A

# FLOW
# D.show() → prints D
# super() → goes to next in MRO → B

# B.show() → prints B
# super() → goes to next in MRO → C

# C.show() → prints C
# sUper() → goes to next in MRO → A
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

### The Diamond Problem Explained 
# DIAMOND PROBLEM - The Diamond Problem is a well-known issue in object-oriented programming (OOP) that arises in languages that support multiple inheritance. It refers to
# the complexity that can occur when a class inherits from two classes that both inherit from the same base class. This creates a "diamond-shaped" inheritance structure and
# This creates ambiguity about which parent’s method should be executed, and may result in the base class method being called multiple times..
# Here’s an illustration of the diamond problem with an example:

# ```
#         A
#        / \
#       B   C
#        \ /
#         D
# ```

# * **Class A** is the top-level class.
# * **Class B** and **Class C** both inherit from **Class A**.
# * **Class D** inherits from both **Class B** and **Class C**.

# Now, let’s consider a method `m()` in `A` that is inherited by both `B` and `C`. When an instance of `D` calls `m()`, there is a question about which method should be executed:

# * Should it use the method from `A` (which is inherited by both `B` and `C`)?
# * Or should it use the method from `B` or `C`?

# This leads to ambiguity, and this situation is called the **Diamond Problem**.

# code showing the problem 
class A:
    def show(self):
        print("A")

class B(A):
    def show(self):
        print("B")
        A.show(self)   # Direct call

class C(A):
    def show(self):
        print("C")
        A.show(self)   # Direct call

class D(B, C):
    def show(self):
        print("D")
        B.show(self)
        C.show(self)

d = D()
d.show() # output - D B A C A
# Since both B and C call A directly, and D calls both B and C, the method in A is executed twice, creating ambiguity and redundancy.

# Explain the Solution (Using super + MRO)
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
d.show() # D B C A
# Python solves the diamond problem using C3 Linearization (MRO - Method Resolution Order).
# When we use super(), Python ensures that each class method is executed only once and follows a specific order:D → B → C → A


# ### How Python Resolves the Diamond Problem

# In Python, the **Diamond Problem** is resolved using the **Method Resolution Order (MRO)**. The MRO is a linear order in which classes are searched when a method 
# is called on an object. Python uses a specific algorithm called the **C3 Linearization** to establish the MRO.

# #### C3 Linearization:

# C3 Linearization is an algorithm used by Python to resolve the method resolution order in the case of multiple inheritance. It ensures that:

# 1. A class appears before its parents.
# 2. The inheritance order is respected.
# 3. It avoids ambiguity by giving precedence to the classes in the leftmost (first) inheritance path.

# In Python, you can view the MRO of a class by using the `mro()` method or the `__mro__` attribute.

### Example: Viewing the MRO

# ```python
class A:
    def method(self):
        print("Method in A")

class B(A):
    def method(self):
        print("Method in B")

class C(A):
    def method(self):
        print("Method in C")

class D(B, C):  # D inherits from both B and C
    pass

# Check the Method Resolution Order (MRO)
print(D.mro())  # or print(D.__mro__)

# Now, let's call the method on an instance of D
d = D()
d.method()
# ```

#### Output:

# ```python
# [<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]
# Method in B
# ```

# * The MRO shows that Python will search the method in the following order:

#   1. `D`
#   2. `B`
#   3. `C`
#   4. `A`
#   5. `object` (this is the base class of all Python classes)

# * When `d.method()` is called, Python searches for the `method()` in `D`, then `B`, and it finds it in `B`. So, **`Method in B`** is printed.

# ### How Python Resolves the Diamond Problem: MRO and C3 Linearization

# Python's **C3 Linearization** ensures that:

# * The **left-to-right inheritance** order is followed.
# * The **deepest classes** are searched first (i.e., classes that are inherited directly before the parent classes).
# * The **same class is not visited twice** during the resolution process.

# ### Why Python’s MRO Solves the Diamond Problem

# * **No ambiguity**: Because Python’s MRO ensures a consistent and unambiguous order in which classes are checked, it solves the Diamond Problem.
# * **Customizable**: You can control the inheritance order and method resolution path by adjusting the order of inheritance in the class definition.

# ### Conclusion

# * The **Diamond Problem** arises in **multiple inheritance** when a class inherits from multiple classes that share a common ancestor, leading to ambiguity about which method to call.
# * Python resolves this problem using **C3 Linearization** and the **Method Resolution Order (MRO)**, which defines a consistent order in which classes are searched for a method.
# * The MRO can be checked using `ClassName.mro()` or `ClassName.__mro__`.
# * By following this method, Python avoids ambiguity and ensures that the **leftmost path** in the inheritance chain is given precedence.
