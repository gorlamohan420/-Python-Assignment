def divide(a, b):
    try:
        result = a / b
        print("Result of division:", result)
    except ZeroDivisionError:
        print("Error: Division by zero occurred!")
    finally:
        print("Executing finally block")
divide(10, 2) 
print("--------------------")
divide(10, 0)  