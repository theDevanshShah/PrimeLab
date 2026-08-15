# # ============================================================
# #  STRINGS IN PYTHON: Knowledge, Facts, Trivia & Examples
# # ============================================================

# # FACT 1: Strings are IMMUTABLE
# # Once created, you cannot change a string. Any operation creates a NEW string.
# # This is a memory optimization in Python's design.

# original = "hello"
# # original[0] = 'H'  # ❌ TypeError: 'str' object does not support item assignment
# new_string = "h" + original[1:]  # ✅ Creates new string instead
# print(f"Original: {original}, New: {new_string}")


# # ============================================================
# #  SECTION 1: STRING BASICS
# # ============================================================

# # Convention: Single quotes for single chars, double quotes for words
# # (Not enforced, but makes code readable)
# char = 'a'
# word = "python"
# sentence = "I love coding in Python"

# print(f"Char: {char}, Word: {word}, Sentence: {sentence}")


# # FACT 2: Strings are sequences (like lists)
# # Each character has an index starting from 0
# #
# # Index:     0 1 2 3 4 5
# # String:    p y t h o n
# # Rev Index: -6-5-4-3-2-1

# word = "python"
# print(f"First char: {word[0]}")      # p
# print(f"Last char: {word[-1]}")      # n
# print(f"Third char: {word[2]}")      # t


# # ============================================================
# #  SECTION 2: LENGTH, CONCATENATION & REPETITION
# # ============================================================

# # len() - Get length of string
# text = "Python"
# print(f"Length of '{text}': {len(text)}")  # 6

# # EXPERIENCE: Common mistake - confusing len() for lists vs strings
# # Both use len() but strings have no .append()

# # Concatenation - Join strings with +
# greeting = "Hello" + " " + "World"
# print(greeting)  # Hello World

# # TRIVIA: Strings can be concatenated, but not with non-string types
# # age = 25
# # message = "I am " + age  # ❌ TypeError
# message = "I am " + str(25)  # ✅ Convert to string first

# # Repetition - Repeat strings with *
# laugh = "Ha" * 3
# print(laugh)  # HaHaHa

# # KNOWLEDGE: Efficient string building - use join() not +
# # ❌ Inefficient (creates new string each time)
# result = ""
# for word in ["Hello", "World", "Python"]:
#     result = result + " " + word

# # ✅ Efficient (builds in one operation)
# words = ["Hello", "World", "Python"]
# result = " ".join(words)
# print(result)


# # ============================================================
# #  SECTION 3: INDEXING & SLICING
# # ============================================================

# text = "Python"

# # Single indexing
# print(f"text[0] = {text[0]}")      # P
# print(f"text[1] = {text[1]}")      # y
# print(f"text[-1] = {text[-1]}")    # n (last)
# print(f"text[-2] = {text[-2]}")    # o (second last)

# # Slicing: string[start:end:step]
# # FACT: end index is EXCLUSIVE (not included)
# print(f"text[0:3] = {text[0:3]}")    # Pyt (indices 0,1,2)
# print(f"text[2:5] = {text[2:5]}")    # tho (indices 2,3,4)
# print(f"text[:3] = {text[:3]}")      # Pyt (from start to 2)
# print(f"text[3:] = {text[3:]}")      # hon (from 3 to end)
# print(f"text[::2] = {text[::2]}")    # Pto (every 2nd char)

# # TRIVIA: Reverse string using slicing
# reversed_text = text[::-1]  # nohtyP
# print(f"Reversed: {reversed_text}")

# # EXPERIENCE: String slicing never raises IndexError
# # Out of bounds indices are silently ignored
# print(text[0:100])  # Python (no error, just returns up to end)
# print(text[-100:3])  # Pyt (no error)


# # ============================================================
# #  SECTION 4: STRING METHODS (SUPER IMPORTANT!)
# # ============================================================

# # upper() - Convert to uppercase
# text = "python"
# print(text.upper())  # PYTHON
# print("Hello".upper())  # HELLO

# # lower() - Convert to lowercase
# text = "PYTHON"
# print(text.lower())  # python
# print("Hello".lower())  # hello

# # capitalize() - First char uppercase, rest lowercase
# text = "hELLO wORLD"
# print(text.capitalize())  # Hello world

# # title() - First char of each word uppercase
# text = "hello world python"
# print(text.title())  # Hello World Python

# # FACT: These methods don't change original (strings are immutable)
# original = "Hello"
# result = original.lower()
# print(f"Original: {original}, Result: {result}")  # Different strings!


# # ============================================================
# #  SECTION 5: SEARCHING & FINDING
# # ============================================================

text = "The quick brown fox jumps over the lazy dog"

# # find() - Returns index of first occurrence, -1 if not found
print(text.find("quick"))  # 4
print(text.find("the"))    # 31
print(text.find("xyz"))    # -1 (not found)

# # EXPERIENCE: find() vs in
# # Use 'in' for checking existence, find() for getting position
# if "fox" in text:
#     print("Found!")
# index = text.find("fox")
# print(f"Position: {index}")  # 16

if "jumps" in text:
    print("Found it exists on this index : ", text.find("jumps"))
else:
    print("Not Found")
    
# # count() - Count occurrences
# sentence = "apple apple banana apple"
# print(sentence.count("apple"))  # 3

sentence = "A dog is a loyal friend of human beings."
print(sentence.count("a"))

# # startswith() & endswith()
# word = "python"
# print(word.startswith("py"))  # True
# print(word.endswith("on"))    # True

someWord = "Organization"
print(someWord.startswith("Or")) # True
print(someWord.startswith("or")) # False
print(someWord.endswith("on")) # True

# # ============================================================
# #  SECTION 6: REPLACING & SPLITTING
# # ============================================================

# # replace() - Replace substring
# text = "I like apples, apples are sweet"
# new_text = text.replace("apples", "oranges")
# print(new_text)  # I like oranges, oranges are sweet

text = "I love my ex gf. My ex gf is beautiful"
new_text = text.replace("ex","current")
print(new_text)

# # FACT: replace() replaces ALL occurrences by default
# text = "banana"
# print(text.replace("a", "o"))  # bonono (all 3 a's replaced)/

text = "I love my ex gf. My ex gf is beautiful"
new_text = text.replace("ex","current", 1)
print(new_text)


# # Replace only first N occurrences
# text = "banana"
# print(text.replace("a", "o", 1))  # bonana (only first a)
# print(text.replace("a", "o", 2))  # bonona (first two a's)

# # split() - Split string into list
# sentence = "Python is awesome"
# words = sentence.split()  # Splits by spaces by default
# print(words)  # ['Python', 'is', 'awesome']

# # Split by specific character
# csv_data = "apple,banana,orange,mango"
# fruits = csv_data.split(",")
# print(fruits)  # ['apple', 'banana', 'orange', 'mango']

# # EXPERIENCE: split() vs split(", ")
# text = "apple, banana, orange"
# print(text.split(","))   # ['apple', ' banana', ' orange'] (extra spaces)
# print(text.split(", "))  # ['apple', 'banana', 'orange'] (clean)

# # join() - Opposite of split (join list into string)
# fruits = ["apple", "banana", "orange"]
# result = ", ".join(fruits)
# print(result)  # apple, banana, orange

# # TRIVIA: join() is faster than + for combining many strings
# # Best practice: always use join() for string building


# # ============================================================
# #  SECTION 7: WHITESPACE OPERATIONS
# # ============================================================

# # strip() - Remove whitespace from both ends
# text = "  hello world  "
# print(f"'{text.strip()}'")      # 'hello world'
# print(f"'{text.lstrip()}'")     # 'hello world  '
# print(f"'{text.rstrip()}'")     # '  hello world'

# # EXPERIENCE: Common use case - cleaning user input
# user_input = "  john doe  "
# clean_name = user_input.strip()

# # Remove specific characters
# text = "xxxHelloxxx"
# print(text.strip("x"))  # Hello


# # ============================================================
# #  SECTION 8: STRING CHECKING METHODS
# # ============================================================

# # isdigit() - Check if all characters are digits
# print("12345".isdigit())    # True
# print("123a5".isdigit())    # False

# # isalpha() - Check if all characters are alphabetic
# print("hello".isalpha())    # True
# print("hello123".isalpha()) # False

# # isalnum() - Check if alphanumeric (letters + digits)
# print("hello123".isalnum()) # True
# print("hello 123".isalnum()) # False (has space)

# # isspace() - Check if all whitespace
# print("   ".isspace())      # True
# print(" a ".isspace())      # False

# # isupper() & islower()
# print("HELLO".isupper())    # True
# print("hello".islower())    # True
# print("Hello".isupper())    # False

# # isidentifier() - Check if valid Python variable name
# print("my_var".isidentifier())     # True
# print("123var".isidentifier())     # False (starts with digit)
# print("my-var".isidentifier())     # False (has hyphen)


# # ============================================================
# #  SECTION 9: STRING FORMATTING (VERY IMPORTANT!)
# # ============================================================

# # Method 1: Concatenation (old, not recommended)
# name = "Alice"
# age = 25
# message = "My name is " + name + " and I am " + str(age) + " years old"
# print(message)

# # Method 2: % formatting (old style)
# message = "My name is %s and I am %d years old" % (name, age)
# print(message)

# # Method 3: .format() (modern)
# message = "My name is {} and I am {} years old".format(name, age)
# print(message)

# # With named placeholders
# message = "My name is {name} and I am {age} years old".format(name="Bob", age=30)
# print(message)

# # Method 4: f-strings (BEST - Python 3.6+)
# name = "Charlie"
# age = 28
# message = f"My name is {name} and I am {age} years old"
# print(message)

# # KNOWLEDGE: f-strings can do expressions
# x = 10
# y = 20
# print(f"Sum: {x + y}")  # Sum: 30
# print(f"x doubled: {x * 2}")  # x doubled: 20

# # Format numbers
# price = 19.99
# print(f"Price: ${price:.2f}")  # Price: $19.99
# print(f"Percentage: {0.856:.1%}")  # Percentage: 85.6%

# # FACT: f-strings are fastest and most readable


# # ============================================================
# #  SECTION 10: COMMON STRING OPERATIONS
# # ============================================================

# # Check if substring exists
# text = "python programming"
# if "python" in text:
#     print("Found!")

# # Get all occurrences
# text = "apple apple banana apple"
# count = text.count("apple")
# print(f"'apple' appears {count} times")

# # Find first and last position
# text = "hello world hello"
# first = text.find("hello")
# last = text.rfind("hello")
# print(f"First: {first}, Last: {last}")  # First: 0, Last: 12

# # Palindrome check
# def is_palindrome(s):
#     clean = s.lower().replace(" ", "")
#     return clean == clean[::-1]

# print(is_palindrome("racecar"))  # True
# print(is_palindrome("hello"))    # False


# # ============================================================
# #  SECTION 11: ADVANCED: String Escape Sequences
# # ============================================================

# # Newline
# text = "Hello\nWorld"
# print(text)
# # Output:
# # Hello
# # World

# # Tab
# text = "Name\tAge\tCity"
# print(text)  # Name	Age	City

# # Backslash
# path = "C:\\Users\\Documents"
# print(path)

# # Raw strings (ignore escape sequences)
# path = r"C:\Users\Documents"
# print(path)

# # TRIVIA: Triple quotes for multi-line strings
# bio = """My name is John
# I am a programmer
# I love Python"""
# print(bio)


# # ============================================================
# #  SECTION 12: REAL-WORLD EXAMPLES
# # ============================================================

# # Example 1: Email validation (simple)
# email = "user@example.com"
# if "@" in email and "." in email:
#     print("Looks like valid email")

# # Example 2: Parse CSV data
# csv_line = "John,25,Engineer"
# name, age, job = csv_line.split(",")
# print(f"Name: {name}, Age: {age}, Job: {job}")

# # Example 3: Word frequency counter
# text = "the quick brown fox jumps over the lazy dog the"
# words = text.lower().split()
# word_count = {}
# for word in words:
#     word_count[word] = word_count.get(word, 0) + 1
# print(word_count)
# # {'the': 3, 'quick': 1, 'brown': 1, ...}

# # Example 4: Mask sensitive data
# password = "MySecurePassword123"
# masked = "*" * len(password)
# print(masked)  # ********************

# # Example 5: URL slug generation
# title = "My Awesome Blog Post"
# slug = title.lower().replace(" ", "-")
# print(slug)  # my-awesome-blog-post


# # ============================================================
# #  SECTION 13: EXPERIENCE & GOTCHAS
# # ============================================================

# # GOTCHA 1: String comparison is case-sensitive
# print("Hello" == "hello")  # False
# print("Hello".lower() == "hello".lower())  # True

# # GOTCHA 2: Strings are immutable - reassignment, not modification
# text = "python"
# # text[0] = 'P'  # ❌ Error
# text = "P" + text[1:]  # ✅ Correct way

# # GOTCHA 3: String numbers aren't numbers
# age = "25"
# # age + 5  # ❌ TypeError
# int(age) + 5  # ✅ Convert first

# # GOTCHA 4: split() without argument splits by ANY whitespace
# text = "hello    world"
# print(text.split())      # ['hello', 'world'] (smart)
# print(text.split(" "))   # ['hello', '', '', '', 'world'] (literal)

# # GOTCHA 5: Mutable default arguments in functions (relate to strings)
# # This is a Python gotcha, not string-specific, but important


# # ============================================================
# #  PRACTICE PROBLEMS
# # ============================================================

# # P1: Reverse a string
# word = "python"
# print(f"Reversed: {word[::-1]}")

# # P2: Check if palindrome
# def is_palindrome(word):
#     clean = word.lower().replace(" ", "")
#     return clean == clean[::-1]

# print(is_palindrome("A man a plan a canal Panama"))  # True

# # P3: Count vowels
# text = "python programming"
# vowels = "aeiouAEIOU"
# count = sum(1 for char in text if char in vowels)
# print(f"Vowels: {count}")

# # P4: Find longest word
# words = "the quick brown fox jumps".split()
# longest = max(words, key=len)
# print(f"Longest word: {longest}")

# # P5: Remove duplicates, preserve order
# text = "hello"
# seen = set()
# result = ""
# for char in text:
#     if char not in seen:
#         seen.add(char)
#         result += char
# print(f"No duplicates: {result}")  # helo

st = """ Teri report padh ke lag raha hai tu naturally sahi sequence mein seekh raha hai.

Pehle:

1. Water confidence
2. Floating
3. Gliding
4. Kicking
5. Breathing
6. Strokes

Bahut log step 1 skip karke seedha step 6 pe jump karte hain aur struggle karte hain.

Vocabulary word: Incremental = improving little by little over time.

Example:

“Swimming progress is incremental; tiny improvements each session turn into huge gains after a few months.”

Kal ka success metric:

“Kya main aaj pani mein kal se zyada relaxed tha?” """

print(st)

st2 = "Dev"
for character in st2:
    print(character)
    
num_list = "0123456789"

#Let's lear slicing of string in python

print(num_list)
print(num_list[:])
print(num_list[0:5])
print(num_list[2:7])
print(num_list[0:6:2])

# lower case
stringtobelower = "DeVanSH"
print(stringtobelower.lower())


# upper case
stringtobeupper = "DeVanSH"
print(stringtobelower.upper())

# strip
stringtobeStripped = "D.    e Va n SH"
print(stringtobelower.strip().lower())

# Replace
original_string = "I love India."
print(original_string)
changedString = original_string.replace("India","Germany")
print(original_string)
print(changedString)

original_string = "I love Japan."
print(original_string)