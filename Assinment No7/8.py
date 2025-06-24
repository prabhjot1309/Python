#8. Write a function to count the frequency of each word in a given string.
def word_frequency(s):
    words = s.split()
    frequency = {}
    for word in words:
        word = word.lower()  # To make the count case-insensitive
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1
    return frequency
print(word_frequency("Hello world hello"))