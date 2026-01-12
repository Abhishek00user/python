# Getters: Methods that get or return the value of an attribute.
# Setters: Methods that set or update the value of an attribute.
# Purpose: Encapsulation — hide internal data and control how it is accessed or modified.

#isinstance() in Python - It’s a built-in function used to check if an object belongs to a particular class (or a tuple of classes).
# It returns True if the object is an instance (or subclass instance) of the specified class, otherwise False.

print(isinstance(5, int))          # True
print(isinstance(5, (int, float))) # True (matches at least one)


# access modifiers
class student:
    def __init__(self, name, marks):
        self.name = name       # public
        self._marks = marks    # protected
        self.__id = 123        # private



s = student("Abhishek", 95)

print(s.name)      # public → accessible
print(s._marks)    # protected → accessible but conventionally “don’t use outside class”
# print(s.__id)    # private → will raise AttributeError
# Access private variable using name mangling
# print(s._student__id)  # 123  will be printed although vs code is showing error but still runs





# getter setter are used for validating the data 
class Student:
    def __init__(self, name, marks):
        self._name = name
        self._marks = marks

    # Getter
    @property
    def name(self):
        return self._name

    # Setter
    @name.setter
    def name(self, value):
        if isinstance(value, str):
            self._name = value
        else:
            raise ValueError("Name must be a string")

    # Getter for marks
    @property
    def marks(self):
        return self._marks

    # Setter for marks
    @marks.setter
    def marks(self, value):
        if 0 <= value <= 100:
            self._marks = value
        else:
            raise ValueError("Marks must be between 0 and 100")

s = Student("Abhishek", 95)

# Using getters
print(s.name)   # Abhishek
print(s.marks)  # 95

# Using setters
s.name = "Raj"  # works
s.marks = 105   # ValueError: Marks must be between 0 and 100

# getter setters are used to hide internal representation

#they are also used to make an attribute read-only
class Employee:
    def __init__(self, name):
        self._name = name   # private storage

    @property
    def name(self):         # getter only
        return self._name

e = Employee("Abhi")
print(e.name)  # "Abhi"
# e.name = "Raj"  # AttributeError: can't set attribute

# pythonic way is by using @property
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def get_balance(self):
        return self.__balance

    def set_balance(self, amount):
        if amount >= 0:
            self.__balance = amount
