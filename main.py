import numpy as np

# Filtering Numpy arrays with Boolean index lists

np1 = np.array([1,2,3,4,5,6,7,8,9,10])

# x = [True, True, False, False, False, False, False, False, False, False]
#
# print(np1)
# print(np1[x])

# filtered = []
#
# for thing in np1:
#     if thing > 5:
#         filtered.append(True)
#     else:
#         filtered.append(False)
#
# print(np1)
# print(filtered) # [False, False, False, False, False, True, True, True, True, True]
# print(np1[filtered]) # [ 6  7  8  9 10]

# Numpy shortcut

filtered = np1 % 2 == 0 # Get everything which the remainder is 0
print(np1) # [ 1  2  3  4  5  6  7  8  9 10]
print(filtered) # [False  True False  True False  True False  True False  True]
print(np1[filtered]) # [ 2  4  6  8 10]