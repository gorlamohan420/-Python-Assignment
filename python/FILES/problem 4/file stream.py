def read_file_random_access(filename):
    try:
        with open(filename, 'r') as file:
            file.seek(0, 2)  
            file_size = file.tell() 
            print("File size:", file_size)
            positions = [100, file_size // 2, file_size - 200]
            for pos in positions:
                file.seek(pos)  
                data = file.read(100)
                print(f"Data at position {pos}: {data}")

    except FileNotFoundError:
        print("File not found!")
filename = "mohan.txt" 
read_file_random_access(filename)
