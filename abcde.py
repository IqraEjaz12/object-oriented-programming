class BankAccount:
    def __init__(self, account_holder, initial_balance=0):
        self.account_holder = account_holder    # Public
        self._account_number = "ACC123456"      # Protected
        self.__balance = initial_balance        # Private
        self.__pin = "1234"                     # Private

    # Public method to check balance
    def check_balance(self, pin):
        if self.__verify_pin(pin):
            return f"Current balance: ${self.__balance}"
        return "Invalid PIN"

    # Public method to deposit money
    def deposit(self, amount, pin):
        if self.__verify_pin(pin):
            if amount > 0:
                self.__balance += amount
                return f"Deposited ${amount}. New balance: ${self.__balance}"
            return "Deposit amount must be positive"
        return "Invalid PIN"

    # Public method to withdraw money
    def withdraw(self, amount, pin):
        if self.__verify_pin(pin):
            if amount > 0 and amount <= self.__balance:
                self.__balance -= amount
                return f"Withdrew ${amount}. New balance: ${self.__balance}"
            return "Insufficient funds or invalid amount"
        return "Invalid PIN"

    # Private method - only used internally
    def __verify_pin(self, pin):
        return pin == self.__pin

    # Protected method - for internal use
    def _get_account_info(self):
        return f"Account: {self._account_number}, Holder: {self.account_holder}"

# Usage
account = BankAccount("John Doe", 1000)

# print(account.check_balance("1234"))     # Output: Current balance: $1000
# print(account.deposit(500, "1234"))      # Output: Deposited $500. New balance: $1500
# print(account.withdraw(200, "1234"))     # Output: Withdrew $200. New balance: $1300
#
# # These will work but are not recommended
# print(account.account_holder)            # Output: John Doe (public)
# print(account._account_number)           # Output: ACC123456 (protected)

# This won't work - private attribute
# print(account.__balance)               # AttributeError


arsl_account = BankAccount("Arslan")
