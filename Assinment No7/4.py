# 4. Write a function that accepts a list of numbers and returns the maximum and minimum values.
def find_max_min(numbers):
   if not numbers:
       return None
   max_num = min_num = numbers[0]
   for num in numbers:
       if num > max_num:
           max_num = num
       if num < min_num:
           min_num = num
   return max_num, min_num
print(find_max_min([3, 1, 4, 1, 5, 9, 2, 6])) 