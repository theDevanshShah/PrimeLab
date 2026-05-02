# Logical Operators in Python
# Used to combine multiple conditions

# and - True only if BOTH conditions are True
# or  - True if AT LEAST ONE condition is True
# not - Reverses the result (True becomes False, vice versa)

# --- and operator ---
print("--- AND ---")
print(True and True)    # True
print(True and False)   # False
print(False and True)   # False
print(False and False)  # False

age = 25
has_license = True
can_drive = age >= 18 and has_license
print("Can drive:", can_drive)  # True

# --- or operator ---
print("\n--- OR ---")
print(True or True)     # True
print(True or False)    # True
print(False or True)    # True
print(False or False)   # False

is_weekend = True
is_holiday = False
can_relax = is_weekend or is_holiday
print("Can relax:", can_relax)  # True

# --- not operator ---
print("\n--- NOT ---")
print(not True)    # False
print(not False)   # True

is_raining = False
go_outside = not is_raining
print("Go outside:", go_outside)  # True

# --- Combining logical operators ---
age = 25
income = 50000
has_good_credit = True

# Eligible for loan: age > 21 AND (income > 40000 OR good credit)
eligible = age > 21 and (income > 40000 or has_good_credit)
print("Loan eligible:", eligible)  # True

# --- Truthy and Falsy values ---
# Falsy: 0, 0.0, "", None, False, [], {}, ()
# Truthy: everything else

print(bool(0))       # False
print(bool(1))       # True
print(bool(""))      # False
print(bool("hello")) # True
print(bool([]))      # False
print(bool([1, 2]))  # True
print(bool(None))    # False

# --- Short-circuit evaluation ---
# and: stops at first False (doesn't check the rest)
# or:  stops at first True (doesn't check the rest)

# This is safe because 'and' short-circuits:
x = 0
# x != 0 is False, so Python doesn't evaluate 10/x (avoids error)
print(x != 0 and 10 / x > 2)  # False

# --- Practical example ---
username = "dev"
password = "pass123"
is_admin = False

if username == "dev" and password == "pass123":
    print("Login successful!")
    if is_admin:
        print("Welcome, Admin!")
    else:
        print("Welcome, User!")
else:
    print("Invalid credentials")
