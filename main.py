import numpy as np

# Create a 1D numpy array

data_array = np.array([1,2,4,3,5])

num_list = [1,2,3,4,5,6,7]
second_array = np.array(num_list)


print(data_array)

print(second_array)

# Generating random integers

randomness = np.random.randint(0, 10, size=5)
randomness2 = np.random.rand(5)
print(randomness)
print(randomness2)