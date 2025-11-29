import numpy as np

# Copy vs view

# Copy is a copy of your array
# A view is also a copy but it's still connected to the original array

np1 = np.array([0,1,2,3,4,5,6])

# # Create a view
# np2 = np1.view()
#
# print(f'Original NP1 {np1}') # [0 1 2 3 4 5 6]
# print(f'Original NP2 {np2}') # [0 1 2 3 4 5 6]
#
# np1[0] = 41
#
# print(f'Changed NP1 {np1}') # [41  1  2  3  4  5  6]
# print(f'Original NP2 {np2}') # [41  1  2  3  4  5  6]

# If you make a change to the view, the original will also be changed

# Create a Copy

np2 = np1.copy()

print(f'Original NP1 {np1}') # [0 1 2 3 4 5 6]
print(f'Original NP2 {np2}') # [0 1 2 3 4 5 6]
#
np2[0] = 41
#
print(f'Changed NP1 {np1}') # [41  1  2  3  4  5  6]
print(f'Original NP2 {np2}') # [0  1  2  3  4  5  6]

