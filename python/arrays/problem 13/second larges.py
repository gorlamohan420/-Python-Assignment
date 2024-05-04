def second_largest(arr):
    sorted_arr = sorted(arr, reverse=True)
    if len(sorted_arr) > 1:
        return sorted_arr[1]
    else:
        return None
array = [1, 2, 3, 4, 5] 
second_largest_number = second_largest(array)
if second_largest_number is not None:
    print("Second largest number in the array:", second_largest_number)
else:
    print("Array has less than 2 elements")
