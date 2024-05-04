def remove_element(arr, value):
    return [x for x in arr if x != value]
array = [1, 2, 3, 4, 5] 
target_value = 3 
modified_array = remove_element(array, target_value)
print("Modified array after removing", target_value, ":", modified_array)
