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

# Protected attribute (_marks): The attribute is prefixed with a single underscore, which is a convention in Python indicating that this is meant to be protected (not directly
#                                 accessed by outside code). Although it is still technically accessible, it is discouraged to access this directly from outside the class.

# Private attribute (__id): The double underscore before the __id attribute is a Python convention that mangles the attribute's name to make it harder to access directly 
#                             from outside the class (name mangling). This makes it "private"—not accessible using the normal attribute syntax from outside the class.

s = student("Abhishek", 95)

print(s.name)      # public → accessible
print(s._marks)    # protected → accessible but conventionally “don’t use outside class”
# print(s.__id)    # private → will raise AttributeError
print(s._student__id)  # private -> can be accesed using name mangling

Even though we can technically access the private attribute using name mangling, this is generally discouraged because it breaks the encapsulation. The idea is to 
restrict direct access and enforce controlled access via methods.


# getter setter are used for validating the data and it  allows you to control access to the internal data.
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

    # The getter (@property) allows you to access the value of the private attribute (_name or _marks) like a normal attribute, but the actual value is fetched through a method.
    @property
    def marks(self):
        return self._marks

    # The setter ensures that only valid values are assigned to the internal attributes. For example, the marks attribute can only be set to values between 0 and 100, and name must be a string.
    # If invalid data is provided, the setter raises an exception (ValueError).
    @marks.setter
    def marks(self, value):
        if 0 <= value <= 100:  # validating the data
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

 # By using these methods, we hide the internal representation (e.g., _name and _marks) from the outside world and expose them in a controlled way. This is a key part of
# encapsulation: protecting the internal state of an object and exposing only the necessary functionality.

#they are also used to make an attribute read-only
class Employee:
    def __init__(self, name):
        self._name = name   # private storage

    @property
    def name(self):         # getter only , By defining only a getter for the name attribute and not providing a setter, we are ensureing that the name cannot be changed once it has been set. This is a form of encapsulation because it prevents external code from modifying the internal state of an object in an uncontrolled way.
        return self._name

e = Employee("Abhi")
print(e.name)  # "Abhi"
# e.name = "Raj"  # AttributeError: can't set attribute

# pythonic way is by using @property, the normal method
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def get_balance(self):
        return self.__balance

    def set_balance(self, amount):
        if amount >= 0:
            self.__balance = amount
