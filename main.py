import numpy as np

# Search
np1 = np.array([1,2,3,4,5,6,7,8,9,10])

# x = np.where(np1 == 3)
# print(x) # (array([2]),)
# print(x[0]) # [2]
#
# np2 = np.array([1,2,3,4,5,6,7,8,9,10, 3])
# y = np.where(np2 == 3)
# print(y) # (array([ 2, 10]),)
# print(y[0]) # [ 2 10]
# print(np2[y[0]]) # [3 3]

# Return even items
# y = np.where(np1 % 2 == 0)
# print(y)

# Return odd items
z = np.where(np1 % 2 == 1)
print(z) # (array([0, 2, 4, 6, 8]),)