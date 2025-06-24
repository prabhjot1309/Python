#6. Write a Python program that reads a text file and prints its content in reverse order (last line first).
# Read file and print lines in reverse order
with open("file1.txt", "r") as file:
    lines = file.readlines()  # Read all lines into a list
    for line in reversed(lines):  # Loop through the list in reverse
        print(line.strip())  # Remove newline and print
