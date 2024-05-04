
def find_index(arr, target):
    try:
        index = arr.index(target)
        return index
    except ValueError:
        return -1
array = [1, 2, 3, 4, 5] 
target_element = 4
index = find_index(array, target_element)
if index != -1:
    print("Index of", target_element, "in the array:", index)
else:
    print(target_element, "is not found in the array")
