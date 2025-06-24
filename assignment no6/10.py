#10. Given a list of numbers, write a Python program to find all unique elements using sets.
list=[2,1,5,4,6,3,2,4,8,6,9,2]
unique_elements=set(list)
print("Original List:", list)
print("Unique Elements:", unique_elements)


#method2 for goohgle colab

del set # Python now thinks set is a dictionary, not the actual built-in set() function.
list=[2,1,5,4,6,3,2,4,8,6,9,2]
unique_elements=set(list)
print("Original List:", list)
print("Unique Elements:", unique_elements)