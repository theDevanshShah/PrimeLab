# Break & Continue in Python
# Control the flow of loops

# --- break: EXIT the loop immediately ---
# Find the first number divisible by 7 between 1 and 100
i = 1
while i <= 100:
    if i % 7 == 0:
        print("First number divisible by 7:", i)
        break  # stops the loop completely
    i += 1

# --- break with for loop ---
# Search for a name in a list
names = ["Alice", "Bob", "Dev", "Charlie"]
search = "Dev"

for name in names:
    if name == search:
        print(f"Found {search}!")
        break
else:
    print(f"{search} not found")  # runs only if break was NOT hit

# --- continue: SKIP current iteration, go to next ---
# Print all numbers from 1 to 10 except 5
for i in range(1, 11):
    if i == 5:
        continue  # skips print for 5, goes to 6
    print(i, end=" ")
print()

# --- Print only odd numbers ---
for i in range(1, 21):
    if i % 2 == 0:
        continue
    print(i, end=" ")
print()

# --- Difference ---
# break → "I'm done, get me out of this loop"
# continue → "Skip this one, move to the next"

# --- Practical: Input validation ---
while True:
    age = int(input("Enter your age (1-120): "))
    if 1 <= age <= 120:
        break
    print("Invalid age! Try again.")

print("Your age:", age)

# --- Practical: Skip negative numbers ---
numbers = [10, -5, 20, -3, 15, -8, 30]
total = 0

for num in numbers:
    if num < 0:
        continue
    total += num

print("Sum of positive numbers:", total)
