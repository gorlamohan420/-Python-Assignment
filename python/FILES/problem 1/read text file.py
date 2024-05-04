def read_text_file(filename):
    try:
        with open(filename, 'r') as file:
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print("File not found")
filename = "mohan.txt" 
read_text_file(filename)
