def average_of_array(arr):
    if not arr:
        return None
    total_sum = sum(arr)
    average = total_sum / len(arr)
    
    return average

array = [1, 2, 3, 4, 5]
result = average_of_array(array)
if result is not None:
    print("Average of array:", result)
else:
     print("Array is empty")
