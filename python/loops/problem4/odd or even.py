def print_odd_even(start, end):
    print("Odd numbers:")
    for num in range(start, end + 1):
        if num % 2 != 0:
            print(num, end=" ")
    print("\nEven numbers:")
    for num in range(start, end + 1):
        if num % 2 == 0:
            print(num, end=" ")
start_number = 1
end_number = 10
print_odd_even(start_number, end_number)
