# range() Function in Python
# Generates a sequence of numbers

# --- Syntax ---
# range(stop)            → 0 to stop-1
# range(start, stop)     → start to stop-1
# range(start, stop, step) → start to stop-1, incrementing by step

# --- range(stop) ---
print("range(5):", list(range(5)))       # [0, 1, 2, 3, 4]

# --- range(start, stop) ---
print("range(2, 8):", list(range(2, 8))) # [2, 3, 4, 5, 6, 7]

# --- range(start, stop, step) ---
print("range(0, 20, 5):", list(range(0, 20, 5)))  # [0, 5, 10, 15]

# --- Negative step (counting backwards) ---
print("range(10, 0, -1):", list(range(10, 0, -1)))  # [10, 9, 8, ..., 1]

# --- Common use cases ---

# Print even numbers from 0 to 20
print("Even:", list(range(0, 21, 2)))

# Print odd numbers from 1 to 19
print("Odd:", list(range(1, 20, 2)))

# --- range is lazy (memory efficient) ---
# range(1000000) does NOT create a list of 1 million numbers
# It generates them one by one as needed
r = range(1000000)
print(len(r))       # 1000000
print(r[0])         # 0
print(r[999999])    # 999999
# But it takes almost no memory!

# --- Check membership ---
print(5 in range(10))    # True
print(15 in range(10))   # False
