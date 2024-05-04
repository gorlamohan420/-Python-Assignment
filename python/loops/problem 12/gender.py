def print_gender(gender):
    gender_dict = {
        "M": "Male",
        "F": "Female"
    }
    print(gender_dict.get(gender, "Invalid gender"))

print_gender("M") 
print_gender("F")  
print_gender("X")  
