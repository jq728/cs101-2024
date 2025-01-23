input_str = input()
lst=""
for char in input_str:
    if "a"<=char<="z":
        char=chr(ord(char)-32)
        lst += char
    elif "A"<=char<="Z":
        char=chr(ord(char)+32)
        lst+=char
    else:
        lst+=char
print(lst)