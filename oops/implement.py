from abc import ABC, abstractmethod

"""
---------------------------------------------------
ABSTRACTION
---------------------------------------------------
Payment is an abstract base class.
It exposes only WHAT needs to be done (pay),
not HOW it is done.
Implemented using ABC and @abstractmethod.
"""
class Payment(ABC):

    @abstractmethod
    def pay(self, amount: float):
        pass


"""
---------------------------------------------------
INHERITANCE + POLYMORPHISM
---------------------------------------------------
CardPayment inherits from Payment
and provides its own implementation of pay()
"""
class CardPayment(Payment):

    def __init__(self, card_number: str, card_holder: str):
        # ENCAPSULATION:
        # Instance variables are accessed through the class methods
        self._card_number = card_number
        self._card_holder = card_holder

    # Overriding abstract method → polymorphism
    def pay(self, amount: float):
        print(f"Paid {amount} using Card")
        print(f"Card Holder: {self._card_holder}")


"""
Another derived class implementing Payment
"""
class UpiPayment(Payment):

    def __init__(self, upi_id: str):
        self._upi_id = upi_id

    # Polymorphic behavior
    def pay(self, amount: float):
        print(f"Paid {amount} using UPI")


"""
---------------------------------------------------
ENCAPSULATION
---------------------------------------------------
PaymentService encapsulates sensitive data like balance.
Direct access to balance is restricted.
"""
class PaymentService:

    def __init__(self, balance: float):
        self._balance = balance   # hidden data (encapsulation)

    """
    This function processes payment.
    It does not care about the payment type.
    It uses polymorphism via base class reference.
    """
    def process_payment(self, payment: Payment, amount: float):
        if amount <= self._balance:
            payment.pay(amount)   # runtime polymorphism
            self._balance -= amount
        else:
            print("Insufficient balance")


# -------------------------------
# MAIN
# -------------------------------
if __name__ == "__main__":

    # Creating payment service with initial balance
    service = PaymentService(5000)

    """
    Base class reference pointing to derived class objects.
    This enables polymorphism.
    """
    p1 = CardPayment("1234-5678", "Abhishek Raj")
    p2 = UpiPayment("user@upi")

    # Same function call, different behavior
    service.process_payment(p1, 1500)
    service.process_payment(p2, 2000)

# I used Python’s ABC module with @abstractmethod to define what a payment must do, without exposing implementation details.”
# Sensitive data like balance, card number, and card holder are prefixed with _ to indicate internal usage and accessed only through methods.
# Concrete payment types inherit from the Payment abstract base class
# The process_payment method works with any payment type because they all implement pay()