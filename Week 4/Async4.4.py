import numpy as np

# Use index slicing and show how to get the subarray consisting of the last 2 rows, and 3rd and 4th columns
given_array = [1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20]
np_array = np.asarray(given_array).reshape(4, 5)
print("Full array:")
print(np_array)
print("Subarray:")
print(np_array[2:4, 2:4])

# Show how to create a one-dimensional array that sums the columns
col_sums_array = np.asarray(np_array.sum(axis=0)).reshape(1, 5)
print("One dimensional array that sums the columns:")
print(col_sums_array)