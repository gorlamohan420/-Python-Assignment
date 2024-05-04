def contains_value(arr, value):
    return value in arr
array = [1, 2, 3, 4, 5]  
target_value = 3  
if contains_value(array, target_value):
    print("The array contains the value", target_value)
else:
    print("The array does not contain the value", target_value)
