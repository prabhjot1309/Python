#2. Write a function that checks whether a number is prime or not.
def is_prime(n):
   if n <= 1:
       return False
   for i in range(2, int(n**0.5) + 1):
       if n % i == 0:
           return False
   return True
print(is_prime(7)) 



#method 2
def is_prime(n,i=2):
   if n <= 1:
       return False
   if n==i:
         return True
   if n % i==0:
         return False
   return is_prime(n, i + 1)   
                 
n=int(input("Enter No.:")) 
if is_prime(n):
    print(f"{n} is a prime number.")
else:
    print(f"{n} is not a prime number.")     
   