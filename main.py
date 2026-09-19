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