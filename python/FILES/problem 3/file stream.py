def read_file_stream(filename):
    try:
        with open(filename, 'r') as file:
            while True:
                data = file.read(1024)  
                if not data:
                    break  
                print(data, end='')  
    except FileNotFoundError:
        print("File not found!")
filename = "mohan.txt"
read_file_stream(filename)
