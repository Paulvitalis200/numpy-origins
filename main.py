import numpy as np

array = np.array([200,201,208], dtype=np.int64)

array_float = np.array([1.0, 2.4, 3.3], dtype=np.float64)
arr_complex = np.array([1+2j, 3+4j], dtype=np.complex128)

array_bool = np.array([True, False, True], dtype=np.bool_)

array_test = np.array([1, 0, 1, 0], dtype=np.bool_)


arr_str = np.array(['a', 'bc', 'dejjhjf'], dtype='S3')

arr_full_str = np.array(['apple', 'box', 'ketchyp'], dtype='str')

arr_obj = np.array([1, 'a', 3.5], dtype=object)

str_array = array.astype(str)
print(array_float)
print(arr_complex)
print(array_bool)
print(array_test)
print(arr_str)
print(arr_full_str)

print(arr_obj)
print(str_array)

# Output:
# 1.  2.4 3.3]
# 1.+2.j 3.+4.j]

#index array ordering
indexing_arr = np.array([29,39,33,90,10])
indices = np.array([2,3])

print(indexing_arr[indices])

multi_array = np.array([
    [[2,3,4], [30,32,43]],
    [[12,90,10], [12,32,10]]
])


print(multi_array)

zeros_array = np.zeros((3,4))
ones_array = np.ones((2,4))

print(zeros_array)
print(ones_array)



normal_arr = np.arange(12)
reshaped = normal_arr.reshape(3,4)

print(reshaped)



# Indexing and slicing 2D arrays

# Creating a 4x5 array with values from 1 to 20
arr = np.arange(1, 21).reshape(4, 5)

# 1. Extract the element at the third row and fourth column
element1 = arr[2, 3]


# 2. Extract the entire first row
element2 = arr[0, :]


# 3. Extract the entire last column
element3 = arr[:,4]


# 4. Extract a subarray containing the first three rows and the first two columns
element4 = arr[:3, :2]


print(element1)
print(element2)
print(element3)
print(element4)