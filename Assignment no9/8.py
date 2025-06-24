# 8. Create a NumPy array of numbers from 10 to 30. Filter and print only the even numbers using boolean indexing.
import numpy as np
arr = np.arange(10, 31)
even = arr[arr % 2 == 0]
print("Even no.:", even)    
