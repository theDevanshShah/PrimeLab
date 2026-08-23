"""
===============================================================================
                         DICTIONARIES IN PYTHON
===============================================================================
A dictionary is a mutable collection of key-value pairs.

    {key: value, key: value}

Think of it like a real dictionary: a word (the key) maps to its meaning (the
value). Dictionaries are excellent when we want to look up data by a meaningful
label instead of by a numeric position.

Important facts:
    - Keys must be unique and hashable.
    - Values may repeat and can be any Python object.
    - Dictionaries preserve insertion order (Python 3.7+).
    - Dictionaries are mutable: pairs can be added, changed, or removed.
===============================================================================
"""

# ============================================================================
# 1. CREATING DICTIONARIES
# ============================================================================

student = {"name": "Devansh", "age": 24, "course": "Python"}
print("Dictionary:", student)

empty_dictionary = {}
also_empty = dict()
print("Empty dictionaries:", empty_dictionary, also_empty)

# dict() is useful when keys are valid Python-style names.
person = dict(name="Aarav", age=21, city="Delhi")
print("Using dict():", person)

# Create a dictionary from pairs.
prices = dict([("pen", 10), ("book", 80), ("bag", 500)])
print("From pairs:", prices)

# fromkeys() gives every key the same starting value.
subjects = dict.fromkeys(["math", "science", "english"], 0)
print("Using fromkeys():", subjects)


# ============================================================================
# 2. KEYS, VALUES, AND UNIQUE KEYS
# ============================================================================

dict_marks = {
    "dev": 44,
    "ved": 45,
    "subham": 67,
}

print("\nMarks:", dict_marks)
print("Type:", type(dict_marks))
print("Number of pairs:", len(dict_marks))

# A key identifies one value. Repeating a key overwrites the old value.
duplicate_key = {"language": "Java", "language": "Python"}
print("Repeated key keeps the last value:", duplicate_key)

# Keys must be hashable (stable enough to be used for lookup).
valid_keys = {"name": "Devansh", 101: "Roll number", (10, 20): "Coordinates"}
print("Different hashable key types:", valid_keys)
# Invalid example: {[1, 2]: "list key"}  # TypeError: lists are unhashable


# ============================================================================
# 3. READING VALUES
# ============================================================================

print("\n--- Reading values ---")
print("Dev's marks:", dict_marks["dev"])
print("Subham's marks:", dict_marks["subham"])

# [] raises KeyError when the key is absent.
# print(dict_marks["missing"])  # Uncomment to see the error

# get() is safer when a key may not exist. The default is None.
print("Existing key with get():", dict_marks.get("dev"))
print("Missing key with get():", dict_marks.get("missing"))
print("Custom missing value:", dict_marks.get("missing", 0))


# ============================================================================
# 4. ADDING AND UPDATING PAIRS
# ============================================================================

print("\n--- Adding and updating ---")
dict_marks["dev"] = 46  # Existing key: update its value.
dict_marks["prishu"] = 69  # New key: add a new pair.
print("After assignment:", dict_marks)

dict_marks.update({"ved": 55, "devika": 43})
print("After update():", dict_marks)

# The | operator creates a merged dictionary (Python 3.9+).
first = {"a": 1, "b": 2}
second = {"b": 20, "c": 3}
merged = first | second
print("Merged with |:", merged)  # On conflicts, the right side wins.
first |= second
print("Updated in place with |=:", first)


# ============================================================================
# 5. CHECKING FOR KEYS AND VALUES
# ============================================================================

print("\n--- Membership tests ---")
print("Is 'dev' a key?", "dev" in dict_marks)
print("Is 'missing' absent?", "missing" not in dict_marks)

# 'in' checks keys, not values.
print("Is 46 a key?", 46 in dict_marks)
print("Is 46 a value?", 46 in dict_marks.values())

if "dev" in dict_marks and dict_marks["dev"] >= 40:
    print("Dev passed the marks condition")


# ============================================================================
# 6. ITERATING OVER DICTIONARIES
# ============================================================================

print("\n--- Iteration ---")

# A direct loop visits keys.
for student_name in dict_marks:
    print("Key:", student_name)

for mark in dict_marks.values():
    print("Value:", mark)

# items() gives each key and value as a two-item tuple.
for student_name, marks in dict_marks.items():
    print(f"{student_name}: {marks}")

# enumerate() adds a counter to an iterable.
for number, (student_name, marks) in enumerate(dict_marks.items(), start=1):
    print(f"{number}. {student_name} scored {marks}")


# ============================================================================
# 7. DICTIONARY VIEW OBJECTS
# ============================================================================

print("\n--- keys(), values(), and items() ---")
print("Keys:", dict_marks.keys())
print("Values:", dict_marks.values())
print("Items:", dict_marks.items())

# These are dynamic views, not independent lists.
marks_view = dict_marks.values()
dict_marks["new_student"] = 90
print("View reflects later changes:", marks_view)

# Convert to a list when a separate snapshot is wanted.
keys_snapshot = list(dict_marks.keys())
print("Keys snapshot:", keys_snapshot)


# ============================================================================
# 8. REMOVING PAIRS
# ============================================================================

print("\n--- Removing pairs ---")
removal_demo = {"a": 1, "b": 2, "c": 3, "d": 4}

removed_value = removal_demo.pop("b")
print("pop() returned:", removed_value, "| Dictionary:", removal_demo)

# A default prevents KeyError if the key is missing.
print("Safe pop:", removal_demo.pop("missing", "not found"))

last_pair = removal_demo.popitem()
print("popitem() returned:", last_pair, "| Dictionary:", removal_demo)

del removal_demo["a"]
print("After del:", removal_demo)

removal_demo.clear()
print("After clear():", removal_demo)


# ============================================================================
# 9. NESTED DICTIONARIES
# ============================================================================

print("\n--- Nested dictionaries ---")
all_marks = {
    "boys": {"a": 1, "b": 2, "c": 3},
    "girls": {"f": 1, "i": 2, "j": 3},
}
print("Nested dictionary:", all_marks)
print("Boy 'a' mark:", all_marks["boys"]["a"])

inventory = {
    "laptop": {"price": 70000, "stock": 5},
    "phone": {"price": 30000, "stock": 12},
}
for product, details in inventory.items():
    print(f"{product}: price={details['price']}, stock={details['stock']}")


# ============================================================================
# 10. COPYING: SHALLOW VERSUS DEEP
# ============================================================================

print("\n--- Copying dictionaries ---")
original = {"name": "Devansh", "skills": ["Python", "SQL"]}
shallow_copy = original.copy()
shallow_copy["name"] = "New name"
shallow_copy["skills"].append("Git")
print("Original after shallow copy changes:", original)
# The top-level dictionary is separate, but the nested list is shared.

from copy import deepcopy

deep_copy = deepcopy(original)
deep_copy["skills"].append("Docker")
print("Original after deep copy changes:", original)
print("Deep copy:", deep_copy)


# ============================================================================
# 11. DICTIONARY COMPREHENSIONS
# ============================================================================

print("\n--- Dictionary comprehensions ---")
squares = {number: number**2 for number in range(1, 6)}
print("Squares:", squares)

even_squares = {number: number**2 for number in range(1, 11) if number % 2 == 0}
print("Even squares:", even_squares)

names = ["dev", "ved", "subham"]
name_lengths = {name: len(name) for name in names}
print("Name lengths:", name_lengths)


# ============================================================================
# 12. PRACTICAL EXAMPLES
# ============================================================================

print("\n--- Practical examples ---")

# Count frequency of items.
letters = "banana"
frequency = {}
for letter in letters:
    frequency[letter] = frequency.get(letter, 0) + 1
print("Letter frequency:", frequency)

# Group values by category.
words = ["apple", "ant", "ball", "book", "cat"]
grouped = {}
for word in words:
    first_letter = word[0]
    grouped.setdefault(first_letter, []).append(word)
print("Grouped words:", grouped)

# A function can return a dictionary containing named results.
def get_result(marks):
    total = sum(marks.values())
    average = total / len(marks)
    return {"total": total, "average": average, "passed": average >= 40}


result = get_result({"math": 80, "science": 70, "english": 90})
print("Result summary:", result)


# ============================================================================
# 13. COMMON PITFALLS AND FUN FACTS
# ============================================================================

print("\n--- Pitfalls and facts ---")

# A dictionary stores references to objects; it does not automatically copy
# the objects placed inside it.
shared_list = []
bad_start = dict.fromkeys(["first", "second"], shared_list)
bad_start["first"].append("surprise")
print("fromkeys() shares mutable values:", bad_start)

# Use a comprehension when each key needs its own list.
good_start = {key: [] for key in ["first", "second"]}
good_start["first"].append("separate")
print("Separate mutable values:", good_start)

# Keys are unique, but values do not have to be.
print("Repeated values are allowed:", {"one": 1, "uno": 1})

# Dictionary lookup is usually very fast because dictionaries are hash tables.
# This is why dictionaries are preferred for frequent key-based lookups.


# ============================================================================
# 14. WHEN TO USE A DICTIONARY
# ============================================================================

"""
USE A DICTIONARY WHEN:
    - You need to connect labels to values: {"name": "Devansh"}.
    - You need fast lookup by a key.
    - You need to count, group, index, or cache information.
    - You need structured records with named fields.

USE A LIST WHEN:
    - Order and position are the main ideas.
    - Duplicate items are meaningful.

USE A SET WHEN:
    - You only need unique values and fast membership checks.

USE A TUPLE WHEN:
    - The collection is fixed and should not be changed.
"""