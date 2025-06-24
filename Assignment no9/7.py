# 7. Given: arr = np.array([[3, 5], [7, 9]]). Find the sum across rows and columns using axis.
import numpy as np
arr = np.array([[3, 5], [7, 9]])
print(arr)
row_sum= arr.sum(axis=1)
print("sum across rows:",row_sum) 
column_sum= arr.sum(axis=0)
print("sum across column:",column_sum)
