# Assignment Operators in Python
# Used to assign and update values in variables

# Basic assignment
x = 10
print("x =", x)

# Add and assign (x = x + 5)
x += 5
print("x += 5 →", x)   # 15

# Subtract and assign (x = x - 3)
x -= 3
print("x -= 3 →", x)   # 12

# Multiply and assign (x = x * 2)
x *= 2
print("x *= 2 →", x)   # 24

# Divide and assign (x = x / 4)
x /= 4
print("x /= 4 →", x)   # 6.0 (becomes float!)

# Floor divide and assign
x = 25
x //= 4
print("x //= 4 →", x)  # 6

# Modulus and assign
x = 25
x %= 4
print("x %= 4 →", x)   # 1

# Exponent and assign
x = 3
x **= 4
print("x **= 4 →", x)  # 81

# --- Summary Table ---
# Operator   Example     Same As
# =          x = 5       x = 5
# +=         x += 5      x = x + 5
# -=         x -= 5      x = x - 5
# *=         x *= 5      x = x * 5
# /=         x /= 5      x = x / 5
# //=        x //= 5     x = x // 5
# %=         x %= 5      x = x % 5
# **=        x **= 5     x = x ** 5

# --- Practical example: Running total ---
total = 0
total += 100   # first item
total += 250   # second item
total += 75    # third item
print("Total:", total)  # 425

# --- String concatenation with += ---
message = "Hello"
message += " "
message += "World"
print(message)  # Hello World

# --- Counter pattern ---
count = 0
for i in range(5):
    count += 1
print("Count:", count)  # 5
