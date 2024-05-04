def find_duplicates(arr):
    duplicate_dict = {}
    duplicates = []
    for num in arr:
        if num in duplicate_dict:
            duplicate_dict[num] += 1
        else:
            duplicate_dict[num] = 1
    for key, value in duplicate_dict.items():
        if value > 1:
            duplicates.append(key)
    return duplicates
array = [1, 2, 3, 4, 2, 5, 3, 6, 4]
duplicate_values = find_duplicates(array)
if duplicate_values:
    print("Duplicate values in the array:", duplicate_values)
else:
    print("No duplicate values found in the array")

