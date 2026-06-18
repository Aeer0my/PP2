# class_methods.py
# Demonstrates instance methods, class methods, and static methods


class BankAccount:
    """Represents a simple bank account."""

    interest_rate = 0.03  # class variable — shared rate for all accounts

    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    # --- Instance Methods (work on individual objects via self) ---

    def deposit(self, amount):
        """Add money to the account."""
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount:.2f}. New balance: ${self.balance:.2f}")

    def withdraw(self, amount):
        """Withdraw money if sufficient funds exist."""
        if amount > self.balance:
            print("Insufficient funds.")
        else:
            self.balance -= amount
            print(f"Withdrew ${amount:.2f}. New balance: ${self.balance:.2f}")

    def get_balance(self):
        """Return current balance."""
        print(f"{self.owner}'s balance: ${self.balance:.2f}")

    def apply_interest(self):
        """Apply the current interest rate to the balance."""
        interest = self.balance * BankAccount.interest_rate
        self.balance += interest
        print(f"Interest applied: +${interest:.2f}. Balance: ${self.balance:.2f}")

    # --- Class Method (works on the class itself via cls) ---

    @classmethod
    def set_interest_rate(cls, new_rate):
        """Update the interest rate for ALL accounts."""
        cls.interest_rate = new_rate
        print(f"Interest rate updated to {new_rate * 100:.1f}%")

    # --- Static Method (utility, no access to instance or class) ---

    @staticmethod
    def validate_amount(amount):
        """Check if an amount is a positive number."""
        return isinstance(amount, (int, float)) and amount > 0


# Using the class
account = BankAccount("Alice", 1000)
account.get_balance()
account.deposit(500)
account.withdraw(200)
account.apply_interest()

# Class method — affects all instances
BankAccount.set_interest_rate(0.05)

# Static method — standalone utility
print(BankAccount.validate_amount(100))    # True
print(BankAccount.validate_amount(-50))   # False
