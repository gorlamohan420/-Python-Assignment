def divide(a, b):
    try:
        result = a / b
        print("Result of division:", result)
    except ZeroDivisionError:
        print("Error: Division by zero occurred!")
    except TypeError:
        print("Error: Unsupported operand type(s) for division")
    except Exception as e:
        print("An unexpected error occurred:", e)
divide(10, 2) 
divide(10, 0) 
divide(10, 'a')
