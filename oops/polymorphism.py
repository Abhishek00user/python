# Method overriding happens at runtime
# Polymorphism is the ability of different objects to respond to the same method call in different ways at runtime.

# RUNTIME POLY VIA INEHERITANCE AND METHOD OVERRIDING
class Animal:
    def sound(self):
        print("Some generic animal sound")

class Dog(Animal):
    def sound(self):
        print("Bark")

class Cat(Animal):
    def sound(self):
        print("Meow")

def make_sound(animal):  # Polymorphism Using a Common Function
    animal.sound()  # works for any object

a = Animal()
d = Dog()
c = Cat()
# The method call is resolved at runtime based on the object type.
d.sound() # Polymorphism Using a Common Function

make_sound(a)  # Some generic animal sound
make_sound(d)  # Bark
make_sound(c)  # Meow


# Duck Typing (NO Inheritance) - if an object has the required method, it’s acceptable.
class FileLogger:
    def log(self):
        print("Logging to file")

class DatabaseLogger:
    def log(self):
        print("Logging to database")

def write_log(logger):
    logger.log()

write_log(FileLogger())
write_log(DatabaseLogger())


#  OPERATOR OVERLOADING
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

p1 = Point(2, 3)
p2 = Point(4, 5)

p3 = p1 + p2
print(p3.x, p3.y)


# Built-in Polymorphism (Same Function, Different Types)
print(len("Python"))
print(len([1, 2, 3, 4]))
print(len({1, 2, 3}))

# POLYMORPHISM USING SUPER
class Animal:
    def speak(self):
        print("Animal sound")

class Dog(Animal):
    def speak(self):
        super().speak()
        print("Dog barks")

d = Dog()
d.speak()


#  COMPILE TIME USING ARGS 
def add(a, b, c=0):
    return a + b + c

print(add(2, 3))
print(add(2, 3, 4))



#  REAL LIFT EXAMPLE 

class CreditCardPayment:
    def pay(self, amount):
        print(f"Paid {amount} using Credit Card")

class UPIPayment:
    def pay(self, amount):
        print(f"Paid {amount} using UPI")

class NetBankingPayment:
    def pay(self, amount):
        print(f"Paid {amount} using Net Banking")

def process_payment(payment, amount):
    payment.pay(amount)

payments = [
    CreditCardPayment(),
    UPIPayment(),
    NetBankingPayment()
]

for p in payments:
    process_payment(p, 1000)


