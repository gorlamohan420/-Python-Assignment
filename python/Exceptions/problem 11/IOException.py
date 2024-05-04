try:
    with open("nonexistent_file.txt", "r") as file:
        data = file.read()
except IOError:
    print("Error: Input/output operation failed!")
