# Practice Examples — Conditionals

# 1. Find the largest of three numbers
a = 10
b = 25
c = 15

if a >= b and a >= c:
    print("Largest:", a)
elif b >= a and b >= c:
    print("Largest:", b)
else:
    print("Largest:", c)

# 2. Check if a year is a leap year
year = 2024

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "is a Leap Year")
else:
    print(year, "is NOT a Leap Year")

# 3. Check if a character is a vowel or consonant
ch = input("Enter a character: ")

if ch in "aeiouAEIOU":
    print(ch, "is a Vowel")
else:
    print(ch, "is a Consonant")

# 4. Simple calculator using if-elif
num1 = float(input("Enter first number: "))
op = input("Enter operator (+, -, *, /): ")
num2 = float(input("Enter second number: "))

if op == "+":
    print("Result:", num1 + num2)
elif op == "-":
    print("Result:", num1 - num2)
elif op == "*":
    print("Result:", num1 * num2)
elif op == "/":
    if num2 != 0:
        print("Result:", num1 / num2)
    else:
        print("Error: Division by zero!")
else:
    print("Invalid operator")
