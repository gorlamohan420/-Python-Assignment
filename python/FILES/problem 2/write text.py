def write_to_text_file(filename):
    try:
        with open(filename, 'w') as file:
            print("Enter text to write to the file (Press Enter to finish):")
            while True:
                line = input()
                if not line:
                    break 
                file.write(line + '\n') 
            print("Text successfully written to", filename)
    except IOError:
        print("Error occurred while writing to the file")
filename = "output.txt"  
write_to_text_file(filename)
