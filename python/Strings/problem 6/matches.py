import re
pattern = r'^[a-zA-Z0-9_]+$'
string = "mohan123"
if re.match(pattern, string):
    print("String matches the pattern")
else:
    print("String does not match the pattern")
