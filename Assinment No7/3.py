#3. Create a function that takes a string as input and returns the number of vowels in it.
def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count
print(count_vowels("Hello! Myself Prabhjot Kaur")) 