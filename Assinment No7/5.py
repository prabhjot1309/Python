#5. Write a Python function to calculate the nth Fibonacci number using recursion.
def fibonacci(n):
   if n <= 0:
      return []
   elif n == 1:
       return [0]
   elif n == 2:
       return [0, 1]
   
   fib_series = [0, 1]
   for i in range(2, n):
       next_value = fib_series[i - 1] + fib_series[i - 2]
       fib_series.append(next_value)
   return fib_series
n= int(input("Enter no: "))
print(fibonacci(n))