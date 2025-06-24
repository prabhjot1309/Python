#7. Write a function that takes a list and returns a new list with only unique elements.
def unique_elements(lst):
    unique_set = set(lst)
    return list(unique_set)

my_list = [1, 2, 2, 3, 4, 4, 5]
print(unique_elements(my_list))
