def find_common_values(arr1, arr2):
    set1 = set(arr1)
    set2 = set(arr2)
    common_values = set1.intersection(set2)
    return list(common_values)
array1 = [1, 2, 3, 4, 5] 
array2 = [3, 4, 5, 6, 7] 
common_values = find_common_values(array1, array2)
if common_values:
    print("Common values between the arrays:", common_values)
else:
    print("No common values found between the arrays")
