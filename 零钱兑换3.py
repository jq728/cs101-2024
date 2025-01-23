def min_coins(n, m, coins):
    dp = [m + 1] * (m + 1)
    dp[0] = 0

    for i in range(1, m + 1):
        for coin in coins:
            if i - coin >= 0:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[m] if dp[m] != m + 1 else -1

n, m = map(int, input().split())
coins = list(map(int, input().split()))
print(min_coins(n, m, coins))
