# Average of Two Numbers
# Formula: average = (num1 + num2) / 2

# --- Method 1: Hardcoded values ---
a = 80
b = 90
average = (a + b) / 2
print(f"Average of {a} and {b} = {average}")  # 85.0

# --- Method 2: User input ---
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

average = (num1 + num2) / 2
print(f"Average of {num1} and {num2} = {average}")

# --- Method 3: Using a function ---
def find_average(x, y):
    return (x + y) / 2

result = find_average(75, 85)
print(f"Average: {result}")  # 80.0

# --- Bonus: Average of multiple numbers ---
n = int(input("\nHow many numbers? "))
total = 0
for i in range(n):
    num = float(input(f"Enter number {i + 1}: "))
    total += num

avg = total / n
print(f"Average of {n} numbers = {avg}")
