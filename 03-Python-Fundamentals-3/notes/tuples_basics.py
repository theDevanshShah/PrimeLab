"""
================================================================================
                            TUPLES IN PYTHON
================================================================================
DEFINITION: A tuple is an immutable, ordered collection of elements.
Once created, it cannot be changed (no adding, removing, or modifying elements).
It's like a read-only list that's also more memory-efficient.
================================================================================
"""

# ============================================================================
# 1. CREATING TUPLES
# ============================================================================

# Method 1: Using parentheses ()
my_tuple = (1, 2, 3, 4, 5)
print("Method 1 - Parentheses:", my_tuple)

# Method 2: Without parentheses (comma does the trick!)
another_tuple = 10, 20, 30, 40
print("Method 2 - No parentheses:", another_tuple)

# Method 3: Empty tuple (remember: need () for empty, or it's not a tuple)
empty_tuple = ()
print("Method 3 - Empty tuple:", empty_tuple)

# Method 4: Single element tuple (⚠️ IMPORTANT: need trailing comma!)
single_element = (42,)  # This is a tuple
print("Method 4 - Single element:", single_element, "| Type:", type(single_element))

# Common mistake: Without the comma, it's just a string/value in parentheses
not_a_tuple = (42)  # This is an int, NOT a tuple
print("Without comma:", not_a_tuple, "| Type:", type(not_a_tuple))

# Method 5: Using tuple() constructor
from_list = tuple([5, 10, 15])
print("Method 5 - From list:", from_list)

from_string = tuple("ABC")
print("Method 5 - From string:", from_string)


# ============================================================================
# 2. ACCESSING ELEMENTS (INDEXING)
# ============================================================================

car_types = ("Black Car", "Green Car", "Blue Car", "Red Car", "Yellow Car")
print("\nOriginal tuple:", car_types)

# Positive indexing (starts from 0)
print("First element [0]:", car_types[0])
print("Third element [2]:", car_types[2])

# Negative indexing (starts from -1, goes backwards)
print("Last element [-1]:", car_types[-1])
print("Second last [-2]:", car_types[-2])

# Accessing doesn't change the tuple (it's immutable)
# ❌ This would fail: car_types[0] = "White Car"  # Error: tuples don't support item assignment


# ============================================================================
# 3. SLICING TUPLES
# ============================================================================

print("\n--- Slicing Operations ---")
print("All except last [0:-1]:", car_types[0:-1])
print("First 3 elements [0:3]:", car_types[0:3])
print("From index 2 to end [2:]:", car_types[2:])
print("Every 2nd element [::2]:", car_types[::2])
print("Reversed [::-1]:", car_types[::-1])
print("Last 2 elements [-2:]:", car_types[-2:])


# ============================================================================
# 4. TUPLE OPERATIONS
# ============================================================================

print("\n--- Tuple Operations ---")

# Length
print("Length:", len(car_types))

# Concatenation (combining tuples with +)
more_cars = ("Pink Car", "White Car")
all_cars = more_cars + car_types
print("Concatenation (+):", all_cars)

# Repetition (repeating tuples with *)
repeated = ("car",) * 3
print("Repetition (*):", repeated)

# Membership test (checking if element exists with 'in')
if "Pink Car" in all_cars:
    print("✓ 'Pink Car' found in all_cars")
    
if "Orange Car" not in all_cars:
    print("✓ 'Orange Car' NOT in all_cars")


# ============================================================================
# 5. TUPLE METHODS (Limited but useful!)
# ============================================================================

print("\n--- Tuple Methods ---")

# count() - count occurrences of an element
numbers = (1, 2, 3, 2, 4, 2, 5)
print("Tuple:", numbers)
print("Count of 2:", numbers.count(2))
print("Count of 5:", numbers.count(5))

# index() - find first position of an element
print("Index of 3:", numbers.index(3))
print("Index of 2:", numbers.index(2))  # Returns first occurrence
# ❌ print(numbers.index(10))  # Would raise ValueError - element not found


# ============================================================================
# 6. TYPE CHECKING
# ============================================================================

print("\n--- Type Checking ---")
print("Type of car_types:", type(car_types))
print("Type of all_cars:", type(all_cars))
print("Type of single_element:", type(single_element))


# ============================================================================
# 7. NESTED TUPLES
# ============================================================================

print("\n--- Nested Tuples ---")

# Tuples can contain other tuples
nested_cars = ("BMW", ("JAGUAR", "AUDI", "TOYOTA"), "MARUTI")
print("Nested tuple:", nested_cars)

# Accessing nested elements
print("First element:", nested_cars[0])
print("Nested tuple:", nested_cars[1])
print("First item in nested tuple:", nested_cars[1][0])
print("Second item in nested tuple:", nested_cars[1][1])

# Deep nesting example
complex_data = (1, (2, (3, 4, 5)), 6)
print("Complex nested:", complex_data)
print("Deep access complex_data[1][1][2]:", complex_data[1][1][2])


# ============================================================================
# 8. TUPLE UNPACKING
# ============================================================================

print("\n--- Tuple Unpacking ---")

# Simple unpacking
coordinates = (10, 20)
x, y = coordinates
print(f"Unpacked: x={x}, y={y}")

# Unpacking with multiple values
rgb_color = (255, 128, 0)
red, green, blue = rgb_color
print(f"RGB unpacked: R={red}, G={green}, B={blue}")

# Unpacking with * (captures remaining elements)
data = (1, 2, 3, 4, 5)
first, *middle, last = data
print(f"First: {first}, Middle: {middle}, Last: {last}")

# Swapping values (elegant Python!)
a, b = 5, 10
print(f"Before swap: a={a}, b={b}")
a, b = b, a  # Tuple unpacking makes this elegant!
print(f"After swap: a={a}, b={b}")


# ============================================================================
# 9. ITERATING OVER TUPLES
# ============================================================================

print("\n--- Iteration ---")

# Basic loop
print("Basic loop:")
tup = (1, 2, 3, 4, 5)
for val in tup:
    print(val, end=" ")
print()

# With index (enumerate)
print("With enumerate:")
colors = ("red", "green", "blue")
for index, color in enumerate(colors):
    print(f"Index {index}: {color}")

# Sum of tuple elements
print("\nSum of (1,2,3,4,5):", sum(tup))
print("Product (using loop):")
product = 1
for val in tup:
    product *= val
print("Product:", product)

# Min and Max
print("Min:", min(tup))
print("Max:", max(tup))


# ============================================================================
# 10. TUPLE COMPREHENSION & GENERATOR EXPRESSIONS
# ============================================================================

print("\n--- Tuple Comprehension & Generators ---")

# Tuple comprehension (creates tuple from list comprehension)
squares_list = [x**2 for x in range(1, 6)]
squares_tuple = tuple(x**2 for x in range(1, 6))
print("Squares as tuple:", squares_tuple)

# Generator expression (memory efficient, doesn't store all at once)
gen = (x**2 for x in range(1, 6))
print("Generator:", gen)
print("Generator to tuple:", tuple(gen))


# ============================================================================
# 11. COMPARISON: TUPLES vs LISTS
# ============================================================================

print("\n--- Tuples vs Lists ---")

tup = (1, 2, 3)
lst = [1, 2, 3]

print("Tuple:", tup, "| Type:", type(tup))
print("List:", lst, "| Type:", type(lst))

# Lists are mutable (can be changed)
lst[0] = 99
print("After lst[0] = 99:", lst)

# Tuples are immutable (cannot be changed)
# ❌ tup[0] = 99  # Would raise TypeError

# Tuples are faster and use less memory
import sys
print(f"\nMemory usage - Tuple: {sys.getsizeof(tup)} bytes")
print(f"Memory usage - List: {sys.getsizeof(lst)} bytes")

# Performance: tuple iteration is slightly faster
import timeit
tuple_time = timeit.timeit("for i in (1,2,3,4,5): pass", number=1000000)
list_time = timeit.timeit("for i in [1,2,3,4,5]: pass", number=1000000)
print(f"Tuple iteration time: {tuple_time:.4f}s")
print(f"List iteration time: {list_time:.4f}s")


# ============================================================================
# 12. TUPLES AS DICTIONARY KEYS
# ============================================================================

print("\n--- Tuples as Dictionary Keys ---")

# Tuples can be dictionary keys (because they're immutable)
coordinates_map = {
    (0, 0): "Origin",
    (1, 2): "Point A",
    (3, 4): "Point B",
    (-1, -1): "Point C"
}

print("Coordinates map:", coordinates_map)
print("Value at (1, 2):", coordinates_map[(1, 2)])

# ❌ Lists cannot be dictionary keys (they're mutable)
# bad_dict = {[1, 2]: "value"}  # TypeError!


# ============================================================================
# 13. PRACTICAL EXAMPLES
# ============================================================================

print("\n--- Practical Examples ---")

# Example 1: Function returning multiple values
def get_person_info():
    return ("Devansh", 24, "Developer")

name, age, profession = get_person_info()
print(f"Person: {name}, Age: {age}, Profession: {profession}")

# Example 2: Fixed configuration data
DATABASE_CONFIG = ("localhost", 5432, "mydb")
host, port, db_name = DATABASE_CONFIG
print(f"DB Config: {host}:{port}/{db_name}")

# Example 3: Coordinate system
def distance_from_origin(point):
    x, y = point
    return (x**2 + y**2) ** 0.5

print("Distance from origin to (3, 4):", distance_from_origin((3, 4)))

# Example 4: Sorting tuples (sorts by first element, then second, etc.)
students = (
    ("Alice", 85),
    ("Bob", 92),
    ("Charlie", 78)
)
sorted_students = sorted(students, key=lambda x: x[1], reverse=True)
print("Students sorted by score:", sorted_students)


# ============================================================================
# 14. COMMON PITFALLS & TRICKS
# ============================================================================

print("\n--- Common Pitfalls & Tricks ---")

# Pitfall 1: Trailing comma confusion
print("With comma:", ("single",), "| Type:", type(("single",)))
print("Without comma:", ("single"), "| Type:", type(("single")))

# Pitfall 2: You CAN modify mutable objects INSIDE tuples
mutable_tuple = ([1, 2], {"a": 1})
mutable_tuple[0].append(3)  # List inside tuple can be modified
print("Modified list inside tuple:", mutable_tuple)
# But you can't replace the list itself: ❌ mutable_tuple[0] = [1, 2, 3]

# Trick 1: Returning multiple values elegantly
def divide_and_remainder(a, b):
    return a // b, a % b  # Implicit tuple

quotient, remainder = divide_and_remainder(17, 5)
print(f"17 ÷ 5 = {quotient} remainder {remainder}")

# Trick 2: Named tuples for cleaner code
from collections import namedtuple
Point = namedtuple('Point', ['x', 'y'])
p = Point(3, 4)
print(f"Named tuple: {p}, x={p.x}, y={p.y}")


# ============================================================================
# 15. FUN FACTS ABOUT TUPLES
# ============================================================================

print("\n--- Fun Facts About Tuples ---")

# Fact 1: Tuples are hashable (lists are not)
t = (1, 2, 3)
print(f"Tuple hash: {hash(t)}")

# Fact 2: Tuple with mutable elements is still a tuple but not hashable
mutable_t = ([1, 2], 3)
try:
    hash(mutable_t)
except TypeError:
    print("Tuples with mutable elements can't be hashed")

# Fact 3: Empty tuples are singletons
empty1 = ()
empty2 = ()
print(f"Empty tuples are same object: {empty1 is empty2}")

# Fact 4: Python uses tuples under the hood
d = {"a": 1, "b": 2}
print("Dictionary items (tuples):", d.items())

# Fact 5: Tuple unpacking with * is powerful
numbers = (1, 2, 3, 4, 5)
first, *rest = numbers
print(f"First: {first}, Rest: {rest}")

_, second, *middle, last = numbers
print(f"Second: {second}, Middle: {middle}, Last: {last}")


# ============================================================================
# 16. WHEN TO USE TUPLES
# ============================================================================

print("\n--- When to Use Tuples ---")
"""
✓ USE TUPLES when:
  - Data should not be modified after creation (immutability is a feature)
  - Using as dictionary keys (need hashable objects)
  - Returning multiple values from a function
  - Performance matters (tuples are faster than lists)
  - Need thread-safe data structures
  - Working with fixed-size collections
  
✓ USE LISTS when:
  - You need to modify data (add, remove, change elements)
  - Building collections dynamically
  - Need more methods available
"""

# ============================================================================