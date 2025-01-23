n = int(input())
day = list(map(int, input().split()))
max_length = 1
current_length = 1

for i in range(1, n):
    if day[i] >= day[i - 1]:
        current_length += 1
        max_length = max(max_length, current_length)
    else:
        current_length = 1

print(max_length)