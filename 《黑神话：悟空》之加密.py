k = int(input())
s = input()
result = []
for i in s:
    if 'a' <= i <= 'z':
        result.append(chr((ord(i) - ord('a') - k) % 26 + ord('a')))
    elif 'A' <= i <= 'Z':
        result.append(chr((ord(i) - ord('A') - k) % 26 + ord('A')))
    else:
        result.append(i)
print(''.join(result))