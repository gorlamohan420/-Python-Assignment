def find_largest(num1, num2, num3):
    largest = num1
    if num2 > largest:
        largest = num2
    if num3 > largest:
        largest = num3
    return largest
number1 = 10
number2 = 20
number3 = 15

largest_number = find_largest(number1, number2, number3)
print("The largest number among", number1, ",", number2, ", and", number3, "is:", largest_number)
