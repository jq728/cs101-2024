k=int(input())
misiles=list(map(int,input().split()))
dp=[0]*k
for i in range(k):
    mx=1
    for j in range(i):
        if misiles[i]<=misiles[j]:
            mx=max(mx,dp[j]+1)
    dp[i]=mx
print(max(dp))