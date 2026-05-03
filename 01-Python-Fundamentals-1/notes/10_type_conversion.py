# Type Conversion & Casting in Python
# Converting one data type to another

# --- Implicit Conversion (Python does it automatically) ---
# Python auto-converts smaller type to larger type to avoid data loss

a = 5       # int
b = 2.5     # float
result = a + b
print(result)         # 7.5
print(type(result))   # <class 'float'> (int was auto-converted to float)

# int + bool
x = 10 + True   # True = 1
print(x)         # 11
print(type(x))   # <class 'int'>

# --- Explicit Conversion (You do it manually using functions) ---

# int() - converts to integer
print(int(3.99))      # 3 (truncates, does NOT round)
print(int(3.14))      # 3
print(int("100"))     # 100 (string to int)
print(int(True))      # 1
print(int(False))     # 0
# print(int("hello"))  # ERROR! Can't convert non-numeric string

# float() - converts to float
print(float(10))       # 10.0
print(float("3.14"))   # 3.14
print(float("100"))    # 100.0
print(float(True))     # 1.0

# str() - converts to string
print(str(100))        # "100"
print(str(3.14))       # "3.14"
print(str(True))       # "True"

# String concatenation requires same type
age = 21
# print("I am " + age + " years old")  # ERROR! Can't concat str + int
print("I am " + str(age) + " years old")   # Works!
print("I am", age, "years old")            # Also works (print auto-converts)
print(f"I am {age} years old")              # f-string (best way!)

# bool() - converts to boolean
print(bool(1))        # True
print(bool(0))        # False
print(bool("hello"))  # True
print(bool(""))       # False
print(bool(None))     # False
print(bool([]))       # False (empty list)
print(bool([1, 2]))   # True (non-empty list)

# --- ord() and chr() - character/ASCII conversion ---
print(ord('A'))   # 65 (ASCII value of 'A')
print(ord('a'))   # 97
print(chr(65))    # 'A'
print(chr(97))    # 'a'

# --- round() - rounding numbers ---
print(round(3.14159))      # 3
print(round(3.14159, 2))   # 3.14
print(round(3.5))          # 4
print(round(4.5))          # 4 (banker's rounding - rounds to nearest even!)

# --- Practical example ---
price = "499.99"
quantity = "3"
total = float(price) * int(quantity)
print(f"Total: Rs.{total}")  # Total: Rs.1499.97
