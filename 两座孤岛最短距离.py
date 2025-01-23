from collections import deque
n=int(input())
l=[list(input())for _ in range(n)]
la=[[False]*n for _ in range(n)]
di=[(0,1),(0,-1),(1,0),(-1,0)]
f=deque()
def dfs(x,y):
    for dx,dy in di:
        nx,ny=x+dx,y+dy
        if 0<=nx<n and 0<=ny<n and  l[nx][ny]=='1':
            l[nx][ny]=2
            f.append((nx,ny))
            dfs(nx,ny)
def solve():
    for i in range(n):
        for j in range(n):
            if l[i][j]=='1':
                f.append((i,j))
                l[i][j]=2
                dfs(i,j)
                return
solve()
def bfs():
    ans=0
    while f:
        for _ in range(len(f)):
            x,y=f.popleft()
            for dx, dy in di:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < n :
                    if l[nx][ny] == '1':
                        return ans
                    elif l[nx][ny]=='0':
                        l[nx][ny]=2
                        f.append((nx,ny))
        ans+=1
print(bfs())