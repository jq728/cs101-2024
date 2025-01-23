r, c = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(r)]
dp = [[0 for _ in range(c)] for _ in range(r)]

def dfs(x, y):
    if dp[x][y]!= 0:
        return dp[x][y]
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    max_path = 1
    for dx, dy in directions:
        new_x, new_y = x + dx, y + dy
        if 0 <= new_x < r and 0 <= new_y < c and matrix[x][y] > matrix[new_x][new_y]:
            path_length = dfs(new_x, new_y) + 1
            max_path = max(max_path, path_length)
    dp[x][y] = max_path
    return max_path

ans = 0
for row in range(r):
    for col in range(c):
        ans = max(ans, dfs(row, col))
print(ans)