# Abstraction is the process of hiding internal implementation details and showing only essential features to the user.

from abc import ABC, abstractmethod

from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def start(self):
        pass

class Car(Vehicle):
    def start(self):
        print("Car starts with key")

class Bike(Vehicle):
    def start(self):
        print("Bike starts with self start")

c = Car()
b = Bike()

c.start()
b.start()

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
