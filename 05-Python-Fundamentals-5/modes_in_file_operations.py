"""
File I/O Modes in Python
=======================

This file explains the different modes used while opening files in Python.

Basic idea:
- A file can be opened in different modes depending on what we want to do.
- We can read, write, append, create, or update a file.
- We can also choose between text mode and binary mode.

Important rule:
- In Python, the mode string tells Python how to open the file.
- Example: "r", "w", "a", "x", "t", "b", "+"

Most common modes:
- "r"  -> read mode
- "w"  -> write mode
- "a"  -> append mode
- "x"  -> create only if it does not exist
- "t"  -> text mode (default)
- "b"  -> binary mode
- "+"  -> read + write/update mode

Examples of combined modes:
- "rt"  -> read in text mode
- "wt"  -> write in text mode
- "at"  -> append in text mode
- "rb"  -> read in binary mode
- "wb"  -> write in binary mode
- "ab"  -> append in binary mode
- "r+"  -> read and write
- "w+"  -> write and read
- "a+"  -> append and read
- "x+"  -> create and read/write

Note:
- When no mode is passed, Python uses "r" by default.
- "t" is also default for text files, so "r" and "rt" are basically the same.
- "b" is used for non-text files like images, audio, PDFs, etc.
- In modern Python, "U" (universal newline mode) is deprecated and not used much.
"""

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
TEXT_FILE = BASE_DIR / "sample.txt"
DEMO_FILE = BASE_DIR / "demo_file.txt"
BINARY_FILE = BASE_DIR / "demo_binary.bin"

# ------------------------------------------------------------------
# 1) Default mode: if you do not pass a mode, Python opens in read mode
# ------------------------------------------------------------------
print("\n--- 1) Default mode (same as 'r') ---")
with open(TEXT_FILE, encoding="utf-8") as f:
    print(f.read())

# ------------------------------------------------------------------
# 2) Read mode: 'r'
# ------------------------------------------------------------------
print("\n--- 2) Read mode ('r') ---")
with open(TEXT_FILE, "r", encoding="utf-8") as f:
    content = f.read()
    print(content)

# Why it matters:
# - Opens the file for reading.
# - If the file does not exist, Python raises FileNotFoundError.
# - This is the safest mode when you only want to read data.

# ------------------------------------------------------------------
# 3) Write mode: 'w'
# ------------------------------------------------------------------
print("\n--- 3) Write mode ('w') ---")
with open(DEMO_FILE, "w", encoding="utf-8") as f:
    f.write("Hello! This file was created using write mode.\n")
    f.write("This mode overwrites the file completely.\n")

with open(DEMO_FILE, "r", encoding="utf-8") as f:
    print(f.read())

# Explanation:
# - 'w' opens the file for writing.
# - If the file already exists, its old content is completely erased.
# - If the file does not exist, Python creates a new file.
# - This is used when you want to replace the whole file.

# ------------------------------------------------------------------
# 4) Append mode: 'a'
# ------------------------------------------------------------------
print("\n--- 4) Append mode ('a') ---")
with open(DEMO_FILE, "a", encoding="utf-8") as f:
    f.write("This text is added using append mode.\n")
    f.write("Append mode does not remove previous content.\n")

with open(DEMO_FILE, "r", encoding="utf-8") as f:
    print(f.read())

# Explanation:
# - 'a' adds new content at the end of the file.
# - It does not delete the old data.
# - If the file does not exist, it is created automatically.

# ------------------------------------------------------------------
# 5) Exclusive create mode: 'x'
# ------------------------------------------------------------------
print("\n--- 5) Create mode ('x') ---")
file_to_create = BASE_DIR / "created_with_x_mode.txt"

try:
    with open(file_to_create, "x", encoding="utf-8") as f:
        f.write("This file was created using x mode.\n")
    print("File created successfully with 'x' mode.")
except FileExistsError:
    print("The file already exists, so 'x' mode refused to overwrite it.")

# Explanation:
# - 'x' means create a new file only if it does not already exist.
# - If the file already exists, it raises FileExistsError.
# - This is useful when you want to prevent accidental overwrite.

# ------------------------------------------------------------------
# 6) Text mode: 't'
# ------------------------------------------------------------------
print("\n--- 6) Text mode ('t') ---")
with open(DEMO_FILE, "rt", encoding="utf-8") as f:
    print(f.read())

# Explanation:
# - 't' is text mode.
# - It is the default when opening normal text files.
# - Text mode handles strings and newlines in a human-friendly way.
# - It is used for .txt, .csv, .json, .py, etc.

# ------------------------------------------------------------------
# 7) Binary mode: 'b'
# ------------------------------------------------------------------
print("\n--- 7) Binary mode ('b') ---")
with open(BINARY_FILE, "wb") as f:
    f.write(b"\x00\x01\x02\x03\x04\x05")

with open(BINARY_FILE, "rb") as f:
    data = f.read()
    print(data)
    print(type(data))

# Explanation:
# - 'b' opens the file in binary format.
# - It reads and writes bytes, not text strings.
# - Binary mode is used for images, videos, audio, zip files, PDFs, etc.

# ------------------------------------------------------------------
# 8) Read + Write mode: 'r+'
# ------------------------------------------------------------------
print("\n--- 8) Read + Write mode ('r+') ---")
with open(DEMO_FILE, "r+", encoding="utf-8") as f:
    content = f.read()
    f.seek(0)
    f.write("[Updated with r+]\n" + content)
    f.truncate()

with open(DEMO_FILE, "r", encoding="utf-8") as f:
    print(f.read())

# Explanation:
# - 'r+' opens the file for both reading and writing.
# - The file must already exist.
# - It does not delete existing content automatically.
# - You can read, move the pointer, and then write.

# ------------------------------------------------------------------
# 9) Write + Read mode: 'w+'
# ------------------------------------------------------------------
print("\n--- 9) Write + Read mode ('w+') ---")
with open(DEMO_FILE, "w+", encoding="utf-8") as f:
    f.write("This is written using w+ mode.\n")
    f.seek(0)
    print(f.read())

# Explanation:
# - 'w+' opens the file for writing and reading.
# - It clears the file first, just like 'w'.
# - Then you can read from the same file after moving the pointer to the start.

# ------------------------------------------------------------------
# 10) Append + Read mode: 'a+'
# ------------------------------------------------------------------
print("\n--- 10) Append + Read mode ('a+') ---")
with open(DEMO_FILE, "a+", encoding="utf-8") as f:
    f.write("This text is added using a+ mode.\n")
    f.seek(0)
    print(f.read())

# Explanation:
# - 'a+' opens the file for appending and reading.
# - New data is added at the end.
# - The pointer is usually at the end, so you often need f.seek(0) before reading.

# ------------------------------------------------------------------
# 11) Create + Read/Write mode: 'x+'
# ------------------------------------------------------------------
print("\n--- 11) Create + Read/Write mode ('x+') ---")
new_x_plus_file = BASE_DIR / "created_with_x_plus_mode.txt"

try:
    with open(new_x_plus_file, "x+", encoding="utf-8") as f:
        f.write("Created using x+ mode.\n")
        f.seek(0)
        print(f.read())
except FileExistsError:
    print("The file already exists, so 'x+' refused to overwrite it.")

# Explanation:
# - 'x+' creates a new file if it does not exist.
# - It then allows both reading and writing.
# - It is like a combination of 'x' and '+' but with the safety of no overwrite.

# ------------------------------------------------------------------
# 12) Binary update modes
# ------------------------------------------------------------------
print("\n--- 12) Binary update modes ---")
with open(BINARY_FILE, "wb+") as f:
    f.write(b"\x10\x20\x30\x40")
    f.seek(0)
    print(f.read())

# Summary of binary update variants:
# - "rb+" -> read and write in binary mode (must already exist)
# - "wb+" -> write and read in binary mode (overwrites file)
# - "ab+" -> append and read in binary mode
# - "xb+" -> create and read/write in binary mode

# ------------------------------------------------------------------
# MODE CHEAT SHEET
# ------------------------------------------------------------------
print("\n--- MODE CHEAT SHEET ---")
print("'r'   -> read only (default)")
print("'w'   -> write only (overwrites)")
print("'a'   -> append only (adds at end)")
print("'x'   -> create only if file does not exist")
print("'t'   -> text mode (default for text files)")
print("'b'   -> binary mode for bytes")
print("'r+'  -> read + write")
print("'w+'  -> write + read (clears file)")
print("'a+'  -> append + read")
print("'x+'  -> create + read/write")
print("'rb'  -> read binary")
print("'wb'  -> write binary")
print("'ab'  -> append binary")
print("'xb'  -> create binary")
print("'rb+' -> read + write binary")
print("'wb+' -> write + read binary")
print("'ab+' -> append + read binary")
print("'xb+' -> create + read/write binary")

print("\nRemember: 't' and 'b' change the data type, while '+' changes the access type.")
print("For normal text files, use 'r', 'w', 'a', 'x' and optionally '+' when needed.")
print("For images and binary data, use 'rb', 'wb', 'ab' and their '+' variants.")

# ------------------------------------------------------------------
# Final note
# ------------------------------------------------------------------
# Python file handling is mostly about two questions:
# 1) What do you want to do? (read / write / append / create)
# 2) What kind of data? (text or binary)
#
# Once you know the answer, selecting the correct mode becomes easy.
#
# Examples:
# - read a .txt file        -> open(file, "r")
# - create a new .txt file   -> open(file, "x")
# - add new lines to a file -> open(file, "a")
# - work with an image      -> open(file, "rb")
# - update file contents    -> open(file, "r+") or "a+"

