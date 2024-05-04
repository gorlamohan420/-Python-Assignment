def remove_duplicates(arr):
    return list(set(arr))
array = [1, 2, 3, 4, 2, 5, 3, 6, 4]  
modified_array = remove_duplicates(array)
print("Array after removing duplicates:", modified_array)
