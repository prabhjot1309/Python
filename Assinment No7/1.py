#1. Write a function to find the factorial of a number using recursion.
def fact(n):
   if n < 0:
       return "Factorial is not defined for negative numbers"
   elif n == 0 or n == 1:
       return 1
   else:
       result = 1
       for i in range(2, n + 1):
           result *= i
       return result
print(fact(9))


#method2 
def factorial(n):
    if(n==1 or n==0):
     return 1
    return n *factorial(n-1)

n= int(input("Enter no.:"))
print(f"the factorial of this no. is:{factorial(n)} ")