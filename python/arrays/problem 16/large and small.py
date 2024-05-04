def difference_largest_smallest(arr):
    if not arr:
        return None
    max_val = arr[0]
    min_val = arr[0]
    for num in arr:
        if num > max_val:
            max_val = num
        elif num < min_val:
            min_val = num
    return max_val - min_val
array = [1, 3, 5, 7, 9] 
difference = difference_largest_smallest(array)
if difference is not None:
    print("Difference between the largest and smallest value in the array:", difference)
else:
    print("Array is empty")
