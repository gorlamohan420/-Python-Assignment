try:
    with open("nonexistent_file.txt", "r") as file:
        data = file.read()
except FileNotFoundError:
    print("Error: File not found!")
