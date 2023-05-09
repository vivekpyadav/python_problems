def print_longest_string():
    str1 = str(input("enter first string:"))
    str2 = str(input("enter second string:"))

    if len(str1) > len(str2):
        print(str1)
    elif len(str2) > len(str1):
        print(str2)
    else:
        print(str1)
        print(str2)
print_longest_string()
    
        