from collections import deque
def can_reach_treasure(m, n, grid):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    queue = deque([(0, 0, 0)])
    visited = set((0, 0))
    while queue:
        x, y, steps = queue.popleft()
        if grid[x][y] == 1:
            return steps

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if 0 <= nx < m and 0 <= ny < n and (nx, ny) not in visited and grid[nx][ny] != 2:
                visited.add((nx, ny))
                queue.append((nx, ny, steps + 1))

    return "NO"

m, n = map(int, input().split())
grid = []
for _ in range(m):
    grid.append(list(map(int, input().split())))

result = can_reach_treasure(m, n, grid)
print(result)