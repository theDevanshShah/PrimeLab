"""
===============================================================================
                         ENCAPSULATION IN PYTHON
===============================================================================

Encapsulation means keeping data and the methods that use it together inside a
class, while controlling how the data is read or changed.

Python uses naming conventions and name mangling for access control:
    public     name       -> normal public access
    protected  _name      -> internal-use convention; not truly private
    private    __name     -> name-mangled to discourage direct access

Encapsulation is useful because a class can validate changes and protect its
internal state instead of allowing every piece of code to modify it freely.
===============================================================================
"""

from BankAccount import BankAccount


# =============================================================================
# 1. CREATING AN ACCOUNT
# =============================================================================

account = BankAccount("Dev", 1_000_000, 1234)

# Public attributes are intended for normal access.
print("Account holder:", account.account_name)

# The single underscore means "internal use" by convention.
# It can still be accessed, but balance changes should use class methods.
print("Starting balance:", account.get_balance())


# =============================================================================
# 2. CONTROLLED ACCESS TO PRIVATE DATA
# =============================================================================

# The PIN is private. This direct access would raise AttributeError:
# print(account.__pin)

# Instead, the class provides a safe check without revealing the PIN.
print("Correct PIN:", account.check_pin(1234))
print("Incorrect PIN:", account.check_pin(9999))

account.set_new_pin(4321)
print("New PIN works:", account.check_pin(4321))

# Name mangling is an implementation detail, not a security feature.
# Avoid this outside the class:
# print(account._BankAccount__pin)


# =============================================================================
# 3. CONTROLLED BALANCE CHANGES
# =============================================================================

account.deposit(5_000)
print("After deposit:", account.get_balance())

account.withdraw(2_000)
print("After withdrawal:", account.get_balance())

# These methods validate input before changing the internal balance.
try:
    account.withdraw(2_000_000)
except ValueError as error:
    print("Rejected withdrawal:", error)

try:
    account.set_new_pin(12)
except ValueError as error:
    print("Rejected PIN:", error)


# =============================================================================
# 4. ACCESS LEVEL SUMMARY
# =============================================================================

print("\n--- Access Level Summary ---")
print("Public: accessible normally, for example account.account_name")
print("Protected: _account_balance signals internal use by convention")
print("Private: __pin is name-mangled inside BankAccount")
print("Best practice: use methods to validate and control changes")
