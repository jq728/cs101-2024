n, a, b, c = map(int,input().split())
dp = [float('-inf')] * (n + 1)
dp[0] = 0
for i in (a, b, c):
    for v in range(i, n + 1):
        dp[v] = max(dp[v - i] + 1, dp[v])
print(dp[-1])