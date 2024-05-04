student_dict = {
    101: 'Mohan',
    102: 'Bharath',
    103: 'Yogesh',
    104: 'Mani',
    105: 'Monish'
}
student_dict[106] = 'Lakshmi'
student_dict[101] = 'Mohan' 
print(student_dict[102])
nested_dict = {
    'A': {'1': 'Apple', '2': 'Ant'},
    'B': {'1': 'Ball', '2': 'Bat'},
    'C': {'1': 'Cat', '2': 'Car'}
}
print(nested_dict['A']['1'])  
print(nested_dict['B']['2'])  
print(student_dict.keys())  
del student_dict[105]
