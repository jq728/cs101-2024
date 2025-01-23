n,b=map(int,input().split())
prices=list(map(int,input().split()))
objs=list(map(int,input().split()))
dp=[[0 for _ in range(b+1)] for _ in range(n+1)]
for i in range(1,n+1):
    for j in range(1,b+1):
        dp[i][j]=dp[i-1][j]
        if j-objs[i-1]>=0:
            dp[i][j]=max(dp[i][j],(prices[i-1]+dp[i-1][j-objs[i-1]]))
print(dp[n][b])