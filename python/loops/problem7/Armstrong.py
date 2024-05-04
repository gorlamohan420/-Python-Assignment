 def is_armstrong(num):
    # Convert the number to a string to count its digits
    num_str = str(num)
    num_digits = len(num_str)
    
    # Calculate the sum of each digit raised to the power of the number of digits
    sum_of_digits = sum(int(digit)**num_digits for digit in num_str)
    
    # Check if the number is equal to the sum of its own digits raised to the power of the number of digits
    return num == sum_of_digits

number= 153  # Example Armstrong number

if is_armstrong(number):
    print(number, "is an Armstrong number")
else:
    print(number, "is not an Armstrong number")
