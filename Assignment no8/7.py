#7. Write a Python program to find and replace a word in a file (e.g., replace 'old' with 'new').
file = open("file1.txt", "r")
text = file.read()
file.close()

text = text.replace("old", "new")

file = open("file2.txt", "w")
file.write(text)
file.close()

print("Word replaced successfully.")
