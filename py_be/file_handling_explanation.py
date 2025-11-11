"""
# Python File Handling: Reading From and Writing to Files

This file provides a comprehensive guide to handling files in Python.
File handling is a crucial skill for any programmer, as it allows your
program to persist data by reading from and writing to files.
"""

# --- 1. The `open()` function and the `with` statement ---
# To work with a file, you first need to open it using the built-in `open()` function.
# The best practice for opening files is to use the `with` statement, which
# automatically handles closing the file for you, even if errors occur.

# Syntax: with open("filename.txt", "mode") as file:
#             ...do something with the file...

print("--- 1. Writing to a new file ---")

# We will create a new file called "example.txt" to use in our examples.
# Mode 'w' stands for "write". If the file already exists, its content will be
# overwritten. If it doesn't exist, it will be created.
try:
    with open("example.txt", "w") as file:
        file.write("Hello, this is the first line.\n")
        file.write("This is the second line.\n")
        file.write("And this is the third.\n")
    print("Successfully created and wrote to example.txt")
except IOError as e:
    print(f"An error occurred during writing: {e}")
print()


# --- 2. Reading from a File ---
# Mode 'r' stands for "read". This is the default mode if you don't specify one.
# The program will raise an error if the file does not exist.

print("--- 2. Reading from a file ---")

try:
    # --- Method A: `read()` - Reads the entire file content into one string ---
    print("--- A. Using read() ---")
    with open("example.txt", "r") as file:
        content = file.read()
        print("Full content of the file:")
        print(content)

    # --- Method B: `readlines()` - Reads all lines into a list of strings ---
    print("--- B. Using readlines() ---")
    with open("example.txt", "r") as file:
        lines = file.readlines()
        print(f"Content as a list of lines: {lines}")
        # You can then process each line
        for line in lines:
            print(f"Line (stripped): {line.strip()}") # .strip() removes leading/trailing whitespace, including '\n'

    # --- Method C: Iterating over the file object (most memory-efficient) ---
    print("--- C. Iterating over the file ---")
    with open("example.txt", "r") as file:
        print("Reading line by line:")
        for line in file:
            print(f"  - {line.strip()}")

except FileNotFoundError:
    print("Error: The file 'example.txt' was not found.")
except IOError as e:
    print(f"An error occurred during reading: {e}")
print()


# --- 3. Appending to a File ---
# Mode 'a' stands for "append". If the file exists, new content will be added
# to the end of the file. If it doesn't exist, it will be created.

print("--- 3. Appending to a file ---")
try:
    with open("example.txt", "a") as file:
        file.write("This is a fourth line, appended to the file.\n")
    print("Successfully appended to example.txt")

    # Let's read the file again to see the result
    with open("example.txt", "r") as file:
        print("File content after appending:")
        print(file.read())
except IOError as e:
    print(f"An error occurred during appending: {e}")
print()


# --- 4. Other Important File Modes ---
# - 'r+': Read and Write. The file pointer is at the beginning. Can overwrite existing content.
# - 'w+': Write and Read. Truncates the file first.
# - 'a+': Append and Read. The file pointer is at the end for writing.
# - 'b': Binary mode (e.g., 'rb' for reading a binary file like an image).
# - 't': Text mode (default).

print("--- 4. Using 'r+' mode (Read and Write) ---")
try:
    with open("example.txt", "r+") as file:
        # Read the first line
        first_line = file.readline()
        print(f"Read first line: {first_line.strip()}")
        # Write something new at the current position
        file.write("--- Overwritten Content ---")
    
    # Read the file again to see the change
    with open("example.txt", "r") as file:
        print("\nFile content after using 'r+':")
        print(file.read())
except IOError as e:
    print(f"An error occurred: {e}")
print()

print("\n--- End of File Handling Explanation ---")
