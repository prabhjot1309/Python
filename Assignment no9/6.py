# 6. Create a NumPy array with 20 random values (0 to 1) using np.random.rand(). Find the mean,
# median, standard deviation, min, and max.
import numpy as np
arr= np.random.rand(20)
print(arr)

print(np.mean(arr))  #mean
print(np.median(arr))  #median
print(np.std(arr))  #standard deviation
print(np.min(arr)) #min
print(np.max(arr))  #max