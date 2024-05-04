def compare_numbers(num1, num2):
  
    if num1 < num2:
        print(num1, "is less than", num2)
    else:
        print(num1, "is not less than", num2)
  
    if num1 <= num2:
        print(num1, "is less than or equal to", num2)
    else:
        print(num1, "is not less than or equal to", num2)
  
    if num1 > num2:
        print(num1, "is greater than", num2)
    else:
        print(num1, "is not greater than", num2)
        
    if num1 >= num2:
        print(num1, "is greater than or equal to", num2)
    else:
        print(num1, "is not greater than or equal to", num2)
number1 = 5
number2 = 7

compare_numbers(number1, number2)
