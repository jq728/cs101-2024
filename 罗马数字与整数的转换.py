def int_to_roman(num):
    val = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    syb = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    roman_num = ''
    i = 0
    while num > 0:
        for _ in range(num // val[i]):
            roman_num += syb[i]
            num -= val[i]
        i += 1
    return roman_num

def roman_to_int(s):
    roman_num = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    num = 0
    i = 0
    while i < len(s):
        if i + 1 < len(s) and roman_num[s[i]] < roman_num[s[i + 1]]:
            num += roman_num[s[i + 1]] - roman_num[s[i]]
            i += 2
        else:
            num += roman_num[s[i]]
            i += 1
    return num

input_str = input()
if input_str.isdigit():
    print(int_to_roman(int(input_str)))
else:
    print(roman_to_int(input_str))