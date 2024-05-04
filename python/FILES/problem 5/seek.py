def read_file_to_index(filename, index):
    try:
        with open(filename, 'r') as file:
            file.seek(index)  
            data = file.read() 
            print("Data from index", index, "to end of file:")
            print(data)
    except FileNotFoundError:
        print("File not found")
filename = "mohan.txt" 
index = 50 
read_file_to_index(filename, index)
