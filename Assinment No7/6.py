#6. Create a function that accepts two numbers and returns their greatest common divisor (GCD)
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
print(gcd(46, 18)) 


#method 2
import math
def find_gcd(a, b):
    return math.gcd(a, b)
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print("The GCD is:", find_gcd(num1, num2))