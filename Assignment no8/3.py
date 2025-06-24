#3. Write a Python program to count the number of words in a given text file.
file = open("example.txt", "r")
words = file.read().split()
print("Number of words:", len(words))
file.close()