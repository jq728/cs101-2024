def dfs(x,y):
    if board[x][y]==".":
        return 0
    res, board[x][y]=1,"."
    for d in directions:
        if 0 <= x + d[0] < n and 0 <= y + d[1] < m:
            res += dfs(x + d[0],y + d[1])
    return res
T=int(input())
for _ in range(T):
    n,m=map(int,input().split())
    board,ans=[],0
    for _ in range(n):
        board.append(list(input()))
    directions =[[1,0],[1,1],[0,1],[-1,1],[-1,0],[-1,-1],[0,-1],[1,-1]]
    for i in range(n):
        for j in range(m):
            ans =max(ans,dfs(i,j))
    print(ans)