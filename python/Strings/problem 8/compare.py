def starts_with(string, prefix):
    return string[:len(prefix)] == prefix
string = "gorla mohan"
prefix = "gorla"
if starts_with(string, prefix):
    print("String starts with prefix")
else:
    print("String does not start with prefix")
    
def ends_with(string, suffix):
    return string[-len(suffix):] == suffix

string = "gorla mohan"
suffix = "mohan"
if ends_with(string, suffix):
    print("String ends with suffix")
else:
    print("String does not end with suffix")

def compare_to(string1, string2):
    if string1 == string2:
        return 0
    elif string1 < string2:
        return -1
    else:
        return 1
string1 = "gorla"
string2 = "mohan"
result = compare_to(string1, string2)
if result == 0:
    print("Strings are equal")
elif result < 0:
    print("String1 comes before string2")
else:
    print("String1 comes after string2")

