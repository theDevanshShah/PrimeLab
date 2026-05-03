# Taking User Input in Python
# input() function reads input from the keyboard

# --- Basic input ---
# input() ALWAYS returns a string!
name = input("Enter your name: ")
print("Hello,", name)
print(type(name))  # <class 'str'>

# --- Taking numeric input ---
# Must convert string to int/float

age = int(input("Enter your age: "))
print("Next year you'll be", age + 1)

height = float(input("Enter your height (in feet): "))
print("Your height:", height, "feet")

# --- Taking multiple inputs on one line ---
# Using split()
a, b = input("Enter two numbers (space separated): ").split()
print("You entered:", a, "and", b)
print(type(a))  # Still strings!

# Convert both to int
a, b = int(a), int(b)
print("Sum:", a + b)

# One-liner for multiple int inputs
x, y = map(int, input("Enter two integers: ").split())
print("Product:", x * y)

# --- Input with default message ---
color = input("Favorite color (press Enter for Blue): ") or "Blue"
print("Color:", color)

# --- Practical examples ---

# 1. Simple calculator
print("\n--- Simple Calculator ---")
num1 = float(input("Enter first number: "))
operator = input("Enter operator (+, -, *, /): ")
num2 = float(input("Enter second number: "))

if operator == "+":
    print("Result:", num1 + num2)
elif operator == "-":
    print("Result:", num1 - num2)
elif operator == "*":
    print("Result:", num1 * num2)
elif operator == "/":
    if num2 != 0:
        print("Result:", num1 / num2)
    else:
        print("Error: Cannot divide by zero!")
else:
    print("Invalid operator!")

# 2. Temperature converter
print("\n--- Temperature Converter ---")
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9 / 5) + 32
print(f"{celsius}°C = {fahrenheit}°F")
