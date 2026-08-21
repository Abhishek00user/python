# Abstraction is the process of hiding internal implementation details and showing only essential features to the user.

from abc import ABC, abstractmethod

from abc import ABC, abstractmethod

# Vehicle is an abstract base class that inherits from ABC (Abstract Base Class). This marks the Vehicle class as an abstract 
# class, meaning it is intended to be a blueprint for other classes and cannot be instantiated directly.
# It cannot be used to create objects unless its abstract methods are implemented by a subclass.

class Vehicle(ABC):  #this abstract class can contain both concrete and abstract method

    @abstractmethod
    def start(self):         # start method is abstract method
          pass               # the start method defines a general action (i.e., starting a vehicle) without specifying how it should be done

class Car(Vehicle): # Car is a concrete class here .A concrete class is a class that has no abstract methods and can be instantiated to create objects and it provides the full implementation for all of its methods and does not leave any methods undefined or abstract
    def start(self): # A concrete method is a method that has an implementation(fully defined) in a class
        print("Car starts with key")

class Bike(Vehicle):
    def start(self):
        print("Bike starts with self start")

c = Car()
b = Bike()

c.start()
b.start()   # polymorphism used here because even though both Car and Bike implement the same method start, each one behaves differently according to its specific implementation.

# The Car and Bike classes are concrete subclasses of Vehicle. They inherit from Vehicle and provide specific implementations for 
# the start method.This is where abstraction is applied: the Vehicle class provides the common interface (start), but each subclass
#  provides its own implementation for how that start functionality works.



# 9️⃣ why do abstract class can have concrete methods if they cannot be instantiated?
# ANS->concrete method allows for code reuse and encapsulation of default behavior by inheriting shared behavior, making it easier to create subclasses that don't need to reimplement common functionality
from abc import ABC, abstractmethod

# Abstract class
class Vehicle(ABC):

    # Abstract method that must be implemented by subclasses
    @abstractmethod
    def start(self):
        pass

    # Concrete method with default behavior, that don't need to be changed.common for all the subclasses.it also avoid duplicating the same code in subclasses and promote reusablity
    def stop(self):
        print("Vehicle stopped.")

# Concrete subclass
class Car(Vehicle): # this subclass inherits the concrete method stop() from the Vehicle class without needing to reimplement it

    # Implementation of the abstract method
    def start(self):
        print("Car starts with key")

# Concrete subclass
class Bike(Vehicle):

    # Implementation of the abstract method
    def start(self):
        print("Bike starts with self start")

# Instantiate subclasses
car = Car()
car.start()  # Car-specific implementation
car.stop()   # Inherited concrete method from Vehicle

bike = Bike()
bike.start()  # Bike-specific implementation
bike.stop()   # Inherited concrete method from Vehicle



#  9️⃣ Abstraction + Polymorphism (POWER COMBINATION)
from abc import ABC, abstractmethod

class Payment(ABC):

    @abstractmethod
    def pay(self, amount):
        pass


class CreditCardPayment(Payment):
    def pay(self, amount):
        print(f"Paid {amount} using Credit Card")


class UPIPayment(Payment):
    def pay(self, amount):
        print(f"Paid {amount} using UPI")


def process_payment(payment: Payment, amount):
    payment.pay(amount)


process_payment(CreditCardPayment(), 1000)
process_payment(UPIPayment(), 2000)
