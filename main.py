import numpy as np


# Slicing numpy arrays

np1 = np.array([1,2,3,4,5,6,7,8,9])

# Return 2, 3, 4, 5
print(np1[1:5])

# Return from something till the end of the array?
print(np1[3:])

# Return Negative Slices
# 7, 8
print(np1[-3:-1])

# Steps
print(np1[1:5:2]) # [2 4]

# Steps on the entire arrray
# [1 3 5 7 9]
print(np1[::2])

# Slice a 2-d array
np2 = np.array([[1, 2, 3, 4, 5], [6, 7, 8 ,9, 10]])
# Pull out a single item
print(np2[0, 1])

# Output: 2

# Slice a 2-d array
print(np2[0:1, 1:3]) # This means from the first subarray to the row just before the second one and slice from 1 to 3.

# Output: [[2 3]]

# Slice from both rows
print(np2[0:2, 1:3])

# Output: [[2 3]
#  [7 8]]