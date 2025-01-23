def max_weapon_diff(p, costs):
    n = len(costs)
    dp = [[-float('inf')] * (p + 1) for _ in range(n + 1)]
    dp[0][p] = 0

    for i in range(1, n + 1):
        cost = costs[i - 1]
        for j in range(p + 1):
            if j >= cost:
                dp[i][j - cost] = max(dp[i][j - cost], dp[i - 1][j] + 1)
            else:
                dp[i][j] = max(dp[i][j], dp[i - 1][j])

    return max(dp[n])

p = int(input())
costs = list(map(int, input().split()))
print(max_weapon_diff(p, costs))
