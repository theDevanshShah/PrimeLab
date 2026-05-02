# Operator Precedence in Python
# Determines which operation is performed first in an expression
# (Just like BODMAS/PEMDAS in math!)

# --- Precedence Order (highest to lowest) ---
# 1. ()           Parentheses
# 2. **           Exponentiation
# 3. +x, -x      Unary plus/minus
# 4. *, /, //, %  Multiplication, Division, Floor Div, Modulus
# 5. +, -         Addition, Subtraction
# 6. ==, !=, <, >, <=, >=   Comparisons
# 7. not          Logical NOT
# 8. and          Logical AND
# 9. or           Logical OR

# --- Examples ---

# Without parentheses
result = 2 + 3 * 4
print("2 + 3 * 4 =", result)  # 14 (not 20! multiplication first)

# With parentheses
result = (2 + 3) * 4
print("(2 + 3) * 4 =", result)  # 20

# Exponentiation before multiplication
result = 2 * 3 ** 2
print("2 * 3 ** 2 =", result)  # 18 (3^2=9, then 2*9=18)

# Mixed operations
result = 10 + 20 * 3 / 5 - 2
print("10 + 20 * 3 / 5 - 2 =", result)  # 20.0
# Step by step: 20*3=60, 60/5=12.0, 10+12.0=22.0, 22.0-2=20.0

# Floor division and modulus (same level as * and /)
result = 17 // 3 + 17 % 3
print("17 // 3 + 17 % 3 =", result)  # 5 + 2 = 7

# --- Logical operator precedence ---
# not > and > or

result = True or False and False
print("True or False and False =", result)  # True
# 'and' runs first: False and False = False
# then 'or': True or False = True

result = (True or False) and False
print("(True or False) and False =", result)  # False

# --- Comparison chaining ---
x = 5
print(1 < x < 10)       # True (same as: 1 < x and x < 10)
print(1 < x and x < 10) # True

# --- Rule of thumb ---
# When in doubt, use parentheses!
# It makes code readable AND ensures correct order

# Confusing:
result = 2 ** 3 ** 2  # Right to left! → 2 ** (3**2) → 2 ** 9 = 512
print("2 ** 3 ** 2 =", result)  # 512 (not 64!)

# Clear:
result = (2 ** 3) ** 2  # 8 ** 2 = 64
print("(2 ** 3) ** 2 =", result)  # 64
