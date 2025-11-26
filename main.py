import numpy as np


list1 = [1, 2, 3, 4, 5]

list2 = ["John Elder", 41, list1, True]


# Numpy - Numeric python
# Data type of a numpy array is ndarray = n-dimensional array

np1 = np.array([0, 1, 2, 3, 4, 5])
print(np1)

# Output: [0 1 2 3 4 5]

# Like the len function
print(np1.shape)

# Output: (6,)


# anaother way of creating an array
np2 = np.arange(10)
print(np2)

# Output: [0 1 2 3 4 5 6 7 8 9]

# Step
np3 = np.arange(0, 10, 2)
print(np3)

# Output: [0 2 4 6 8]

# Zeros
np4 = np.zeros(10)
print(np4)

# Output: [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]

# Multidimensional zeros
np5 = np.zeros((2, 10))
print(np5)

# Output: [[0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
#  [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]]

# Full
np6 = np.full((10), 6)
print(np6)

# Output: [6 6 6 6 6 6 6 6 6 6]

# Multidimensional Full
np7 = np.full((2, 10), 6)
print(np7)

# Output: [[6 6 6 6 6 6 6 6 6 6]
#  [6 6 6 6 6 6 6 6 6 6]]

# Convert Python lists to np
my_list = [1, 2, 3, 4, 5]
np8 = np.array(my_list)

print(np8)

# Output: [1 2 3 4 5]

print(np8[0])

# Output: 1