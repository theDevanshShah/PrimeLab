# Arithmetic Operators in Python
# Used to perform mathematical operations

a = 15
b = 4

# Addition
print("a + b =", a + b)    # 19

# Subtraction
print("a - b =", a - b)    # 11

# Multiplication
print("a * b =", a * b)    # 60

# Division (always returns float)
print("a / b =", a / b)    # 3.75

# Floor Division (removes decimal, gives integer result)
print("a // b =", a // b)  # 3

# Modulus (remainder after division)
print("a % b =", a % b)    # 3  (15 = 4*3 + 3)

# Exponentiation (power)
print("a ** b =", a ** b)  # 50625  (15^4)

# --- Important differences ---

# Division vs Floor Division
print(7 / 2)    # 3.5 (true division)
print(7 // 2)   # 3   (floor division - rounds DOWN)

# Floor division with negative numbers (rounds towards -infinity)
print(-7 // 2)  # -4  (not -3!)

# Modulus with negative numbers
print(-7 % 2)   # 1
print(7 % -2)   # -1

# --- Practical examples ---

# Check if a number is even or odd
num = 17
if num % 2 == 0:
    print(num, "is Even")
else:
    print(num, "is Odd")

# Extract last digit of a number
num = 5678
last_digit = num % 10
print("Last digit of", num, "is", last_digit)  # 8

# Extract all digits
num = 5678
print(num % 10)     # 8 (ones)
print(num // 10 % 10)   # 7 (tens)
print(num // 100 % 10)  # 6 (hundreds)
print(num // 1000)       # 5 (thousands)
