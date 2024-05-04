def contains_elements(arr):
    return 12 in arr and 23 in arr
array = [1, 2, 3, 12, 5, 23]
if contains_elements(array):
    print("The array contains both 12 and 23")
else:
    print("The array does not contain both 12 and 23")
