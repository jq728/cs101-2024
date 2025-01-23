def encode_string(s):
    encoded_str = ""
    count = 1
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            encoded_str += f"({s[i-1]},{count})"
            count = 1

    encoded_str += f"({s[-1]},{count})"
    return encoded_str

input_str = input().strip()
a=input_str.lower()
output_str = encode_string(a)
print(output_str)