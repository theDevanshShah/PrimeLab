# Conditional Statements in Python
# Execute different code based on conditions

# --- if statement ---
age = 20
if age >= 18:
    print("You are an adult")

# --- if-else ---
num = 7
if num % 2 == 0:
    print("Even")
else:
    print("Odd")

# --- if-elif-else (multiple conditions) ---
marks = 85

if marks >= 90:
    print("Grade: A")
elif marks >= 80:
    print("Grade: B")
elif marks >= 70:
    print("Grade: C")
elif marks >= 60:
    print("Grade: D")
else:
    print("Grade: F")

# --- Important rules ---
# 1. Colon (:) is required after if/elif/else
# 2. Indentation (4 spaces) defines the code block
# 3. elif and else are optional
# 4. Only ONE block executes (first True condition wins)

# --- Ternary operator (one-line if-else) ---
age = 20
status = "Adult" if age >= 18 else "Minor"
print(status)

# --- Multiple conditions with logical operators ---
age = 25
income = 50000

if age >= 21 and income >= 30000:
    print("Loan approved")
elif age >= 21 or income >= 50000:
    print("Partially eligible")
else:
    print("Not eligible")
