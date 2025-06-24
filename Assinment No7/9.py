#9. Write a function that takes a number and returns True if it is a palindrome, otherwise False.
def is_palindrome(n):
   str_n = str(n)
   return str_n == str_n[::-1]
n=int(input("Enter No.: "))
print(is_palindrome(n))  
