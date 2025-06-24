#7. Write a program to check if a given element is present in a set or not
set ={'apple', 'mango','banana','chiku', 'papaya','kiwi','melon'}
element = input("Enter an element to check: ")

if element in set:
    print(f"{element} is \'present\' in the set.")
else:
    print(f"{element} is \'NOT present\' in the set.")