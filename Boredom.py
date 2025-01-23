n = int(input())
sequence = list(map(int, input().split()))
d = {}
for i in sequence:
    if i not in d:
        d[i] = 1
    else:
        d[i] += 1
N = max(sequence)
dp = [0] * (N + 1)
for i in range(1, N + 1):
    if i in d:
        dp[i] = max(dp[i-2] + i * d[i], dp[i-1])
    if i not in d:
        dp[i] = dp[i-1]
print(dp[-1])
