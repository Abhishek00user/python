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
        B.show(self) # -> it will print B and A
        C.show(self) # -> it will print C and A

d = D()
d.show() # output - D B A C A  

# as we can see the method in A is executed twice , creating ambiguity and redundancy.this is the diamond problem.
# to solve this we use super() which follows the MRO to ensure that each method is called only once and in the correct order.

class A:
    def show(self):
        print("A")

class B(A):
    def show(self):
        print("B")
        super().show() # here super does not mean go to parent class of B, it means Continue searching AFTER B in the ORIGINAL object's MRO

class C(A):
    def show(self):
        print("C")
        super().show()

class D(B, C):
    def show(self):
        print("D")
        super().show() # in this class super() means go to next class in D's MRO(MRO of original  object)

d = D()   # d is the original object and its class is D
d.show() # D B C A
print(D.mro())  #since object belongs to class D so we are printing D's MRO

# This is called cooperative multiple inheritance.

# Every class does part of the work and passes control forward using super().

# This avoids:

# duplicate calls
# skipped classes
# diamond inheritance problems

# This is the core reason super() exists in Python multiple inheritance.