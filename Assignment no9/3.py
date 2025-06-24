#3. Generate an array of 15 random integers between 10 and 100 using np.random.randint. Reshape it into a 3x5 matrix and print it.
import numpy as np
arr = np.random.randint(10, 101, size=15)
matrix = arr.reshape(3, 5)
print("3x5 Matrix of random integers between 10 and 100:")
print(matrix)