def step(n):
    if n==0:
        return 1
    dp=[0]*(n+1)
    dp[0]=1
    for i in range(1,n+1):
        for j in range(i):
            dp[i]+=dp[j]
    return dp[n]
m=int(input())
print(step(m))