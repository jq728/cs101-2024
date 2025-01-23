n = int(input())
f = 1
str = 'I hate it'

for x in range(1, n):
    if f ^ 1:
        str = str.replace('it', 'that I hate it')
    else:
        str = str.replace('it', 'that I love it')

    f ^= 1

print(str)