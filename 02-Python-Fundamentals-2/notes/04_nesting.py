# Nesting in Python
# Putting one if statement inside another

# --- Nested if-else ---
num = int(input("Enter a number: "))

if num >= 0:
    if num == 0:
        print("Zero")
    else:
        print("Positive")
else:
    print("Negative")

# --- Nested example: Grading with attendance ---
marks = 75
attendance = 80

if attendance >= 75:
    if marks >= 90:
        print("Grade A - Excellent!")
    elif marks >= 70:
        print("Grade B - Good")
    elif marks >= 50:
        print("Grade C - Average")
    else:
        print("Grade F - Failed")
else:
    print("Not eligible - Low attendance!")

# --- Nested example: Login system ---
username = input("Username: ")
password = input("Password: ")

if username == "dev":
    if password == "python123":
        print("Login Successful!")
    else:
        print("Wrong password!")
else:
    print("User not found!")

# Tip: Don't nest too deep (max 2-3 levels)
# Use logical operators (and/or) to flatten when possible
# Instead of:
#   if a:
#       if b:
#           do_something()
# Use:
#   if a and b:
#       do_something()
