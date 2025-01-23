def correct_order(expr):
    lst = []
    for char in expr:
        if char.isdigit():
            lst.append(char)
    lst.sort()
    result = '+'.join(lst)
    return result

expr = input()
print(correct_order(expr))