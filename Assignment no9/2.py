#2. Create a 3x3 NumPy array of all zeros and another of all ones. Then create a 3x3 identity matrix.
import numpy as np

zeros_array = np.zeros((3, 3))
print("3x3 Zeros Array:", zeros_array)

ones_array = np.ones((3, 3))
print("\n3x3 Ones Array:", ones_array)


identity_matrix = np.eye(3)
print("\n3x3 Ones identity_matrix:",identity_matrix)