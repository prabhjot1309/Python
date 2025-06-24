# 9. Generate an array of 10 random integers from 1 to 100. Replace all elements greater than 50 with-1.
import numpy as np
arr= np.random.randint(1,101,size=10)
arr[arr>50]=-1
print(arr)