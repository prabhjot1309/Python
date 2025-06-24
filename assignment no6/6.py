# 6. Write a Python program to create two sets and perform union, intersection, and difference operations.
set1={'apple', 'mango','banana','chiku', 'papaya','kiwi','melon'}
set2={'muskmelon', 'strawberry','kiwi','melon'}

union = set1.union(set2)
print("union:", union)
intersection = set1.intersection(set2)
print("intersection:", intersection)
difference = set1.difference(set2)
print("difference:", difference)