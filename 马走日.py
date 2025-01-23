def is_valid(x, y, n, m, visited):
    return 0 <= x < n and 0 <= y < m and not visited[x][y]


def dfs(x, y, n, m, visited, count):
    if count == n * m:
        return 1

    moves = [
        (2, 1), (2, -1), (-2, 1), (-2, -1),
        (1, 2), (1, -2), (-1, 2), (-1, -2)
    ]

    visited[x][y] = True
    total_paths = sum(dfs(x + dx, y + dy, n, m, visited, count + 1)
                      for dx, dy in moves if is_valid(x + dx, y + dy, n, m, visited))
    visited[x][y] = False
    return total_paths


def count_knight_paths(n, m, start_x, start_y):
    visited = [[False] * m for _ in range(n)]
    return dfs(start_x, start_y, n, m, visited, 1)


def main():
    T = int(input())
    for _ in range(T):
        n, m, x, y = map(int, input().split())
        print(count_knight_paths(n, m, x, y))


if __name__ == "__main__":
    main()