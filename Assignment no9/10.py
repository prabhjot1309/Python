#10. Create two arrays: x = np.array([[1, 2], [3, 4]]) and y = np.array([[5, 6], [7, 8]]). Stack them
# vertically and horizontally, then flatten the result into a 1D array.
import numpy as np
x = np.array([[1, 2], [3, 4]]) 
y = np.array([[5, 6], [7, 8]])

v_stack = np.vstack((x, y))
h_stack = np.hstack((x, y))
flattened = h_stack.flatten()
print("Vertical Stack:\n", v_stack)
print("Horizontal Stack:\n", h_stack)
print("Flattened:", flattened)


'''newarr1 = x.reshape(-1)
print(newarr1)

newarr2 = y.reshape(-1)
print(newarr2)'''