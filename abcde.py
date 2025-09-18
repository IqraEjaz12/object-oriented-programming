# class BankAccount:
#     def __init__(self, account_holder, initial_balance=0):
#         self.account_holder = account_holder    # Public
#         self._account_number = "ACC123456"      # Protected
#         self.__balance = initial_balance        # Private
#         self.__pin = "1234"                     # Private
#
#     # Public method to check balance
#     def check_balance(self, pin):
#         if self.__verify_pin(pin):
#             return f"Current balance: ${self.__balance}"
#         return "Invalid PIN"
#
#     # Public method to deposit money
#     def deposit(self, amount, pin):
#         if self.__verify_pin(pin):
#             if amount > 0:
#                 self.__balance += amount
#                 return f"Deposited ${amount}. New balance: ${self.__balance}"
#             return "Deposit amount must be positive"
#         return "Invalid PIN"
#
#     # Public method to withdraw money
#     def withdraw(self, amount, pin):
#         if self.__verify_pin(pin):
#             if amount > 0 and amount <= self.__balance:
#                 self.__balance -= amount
#                 return f"Withdrew ${amount}. New balance: ${self.__balance}"
#             return "Insufficient funds or invalid amount"
#         return "Invalid PIN"
#
#     # Private method - only used internally
#     def __verify_pin(self, pin):
#         return pin == self.__pin
#
#     # Protected method - for internal use
#     def _get_account_info(self):
#         return f"Account: {self._account_number}, Holder: {self.account_holder}"
#
# # Usage
# account = BankAccount("John Doe", 1000)
#
# # print(account.check_balance("1234"))     # Output: Current balance: $1000
# # print(account.deposit(500, "1234"))      # Output: Deposited $500. New balance: $1500
# # print(account.withdraw(200, "1234"))     # Output: Withdrew $200. New balance: $1300
# #
# # # These will work but are not recommended
# # print(account.account_holder)            # Output: John Doe (public)
# # print(account._account_number)           # Output: ACC123456 (protected)
#
# # This won't work - private attribute
# # print(account.__balance)               # AttributeError
#
#
# arsl_account = BankAccount("Arslan")





# class Duck:
#     def make_sound(self):
#         return "Quack!"
#
#     def swim(self):
#         return "Duck swims in water"
#
# class Robot:
#     def make_sound(self):
#         return "Beep boop!"
#
#     def swim(self):
#         return "Robot swims with propellers"
#
# class Dog:
#     def make_sound(self):
#         return "Woof!"
#
#     def swim(self):
#         return "Dog does doggy paddle"
#
# # Function that works with any object that has make_sound and swim methods
# def animal_actions(creature):
#     print(f"Sound: {creature.make_sound()}")
#     print(f"Swimming: {creature.swim()}")
#     print()
#
# # All these work even though they're different types
# duck = Duck()
# robot = Robot()
# dog = Dog()
#
# creatures = [duck, robot, dog]
#
# for creature in creatures:
#     animal_actions(creature)



from abc import ABC, abstractmethod

# Abstract base class
class PaymentProcessor(ABC):
    def __init__(self, merchant_name):
        self.merchant_name = merchant_name

    # Abstract method - must be implemented by child classes
    @abstractmethod
    def process_payment(self, amount):
        pass

    # Abstract method
    @abstractmethod
    def refund_payment(self, transaction_id, amount):
        pass

    # Concrete method - can be used by all child classes
    def send_receipt(self, email, amount):
        return f"Receipt sent to {email} for ${amount}"

# Concrete implementations
class CreditCardProcessor(PaymentProcessor):
    def __init__(self, merchant_name):
        super().__init__(merchant_name)
        self.fee_rate = 0.03  # 3% fee

    def process_payment(self, amount):
        fee = amount * self.fee_rate
        net_amount = amount - fee
        return {
            "status": "success",
            "amount": amount,
            "fee": fee,
            "net_amount": net_amount,
            "method": "Credit Card"
        }

    def refund_payment(self, transaction_id, amount):
        return f"Credit card refund of ${amount} processed for transaction {transaction_id}"

class PayPalProcessor(PaymentProcessor):
    def __init__(self, merchant_name):
        super().__init__(merchant_name)
        self.fee_rate = 0.025  # 2.5% fee

    def process_payment(self, amount):
        fee = amount * self.fee_rate
        net_amount = amount - fee
        return {
            "status": "success",
            "amount": amount,
            "fee": fee,
            "net_amount": net_amount,
            "method": "PayPal"
        }

    def refund_payment(self, transaction_id, amount):
        return f"PayPal refund of ${amount} processed for transaction {transaction_id}"

class BankTransferProcessor(PaymentProcessor):
    def __init__(self, merchant_name):
        super().__init__(merchant_name)
        self.fee_rate = 0.01  # 1% fee

    def process_payment(self, amount):
        fee = amount * self.fee_rate
        net_amount = amount - fee
        return {
            "status": "success",
            "amount": amount,
            "fee": fee,
            "net_amount": net_amount,
            "method": "Bank Transfer"
        }

    def refund_payment(self, transaction_id, amount):
        return f"Bank transfer refund of ${amount} processed for transaction {transaction_id}"

# Usage - client doesn't need to know implementation details
def handle_payment(processor, amount):
    result = processor.process_payment(amount)
    print(f"Payment Method: {result['method']}")
    print(f"Amount: ${result['amount']}")
    print(f"Fee: ${result['fee']:.2f}")
    print(f"Net Amount: ${result['net_amount']:.2f}")
    print()

# Create different processors
credit_processor = CreditCardProcessor("My Store")
paypal_processor = PayPalProcessor("My Store")
bank_processor = BankTransferProcessor("My Store")

processors = [credit_processor, paypal_processor, bank_processor]

# Same interface, different implementations
for processor in processors:
    handle_payment(processor, 100)

    from abc import ABC, abstractmethod


    # --------------------
    # Abstraction
    # --------------------
    class Employee(ABC):
        def __init__(self, name, salary):
            self._name = name  # Encapsulation (protected attribute)
            self._salary = salary

        @abstractmethod
        def get_role(self):
            pass

        def get_details(self):
            return f"Name: {self._name}, Salary: {self._salary}"


    # --------------------
    # Inheritance
    # --------------------
    class Developer(Employee):
        def __init__(self, name, salary, programming_language):
            super().__init__(name, salary)
            self.programming_language = programming_language

        def get_role(self):
            return "Software Developer"

        def write_code(self):
            return f"{self._name} is writing code in {self.programming_language}"


    class Manager(Employee):
        def __init__(self, name, salary, team_size):
            super().__init__(name, salary)
            self.team_size = team_size

        def get_role(self):
            return "Project Manager"

        def manage_team(self):
            return f"{self._name} is managing a team of {self.team_size} members"


    # --------------------
    # Polymorphism
    # --------------------
    def show_employee_work(employee):
        print(f"{employee.get_role()} -> {employee.get_details()}")
        if isinstance(employee, Developer):
            print(employee.write_code())
        elif isinstance(employee, Manager):
            print(employee.manage_team())


    # --------------------
    # Main Program
    # --------------------
    if __name__ == "__main__":
        dev = Developer("Iqra Ejaz", 80000, "Python")
        mgr = Manager("Ali Khan", 120000, 5)

        employees = [dev, mgr]

        for emp in employees:
            show_employee_work(emp)
