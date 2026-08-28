class BankAccount:
    """A bank account that controls access to its sensitive data."""

    def __init__(self, account_name, account_balance, pin):
        if account_balance < 0:
            raise ValueError("Account balance cannot be negative")
        self.account_name = account_name
        self._account_balance = account_balance
        self.__pin = self._validate_pin(pin)

    @staticmethod
    def _validate_pin(pin):
        if not isinstance(pin, int) or not 1000 <= pin <= 9999:
            raise ValueError("PIN must be a four-digit number")
        return pin

    def get_balance(self):
        """Return the balance without exposing the internal attribute."""
        return self._account_balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self._account_balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        if amount > self._account_balance:
            raise ValueError("Insufficient balance")
        self._account_balance -= amount

    def check_pin(self, pin):
        """Check a PIN without returning the stored PIN."""
        return self.__pin == pin

    def set_new_pin(self, new_pin):
        self.__pin = self._validate_pin(new_pin)