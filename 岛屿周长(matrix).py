def circu(n,m,a):
    meter=0
    for i in range(n):
        for j in range(m):
            if a[i][j]==1:
                if i==0 or a[i-1][j]==0:
                    meter+=1
                if i==n-1 or a[i+1][j]==0:
                    meter+=1
                if j==0 or a[i][j-1]==0:
                    meter+=1
                if j==m-1 or a[i][j+1]==0:
                    meter+=1
    return meter
n,m=map(int,input().split())
a=[list(map(int,input().strip().split())) for _ in range(n)]
print(circu(n,m,a))