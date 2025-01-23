def josephus(n, m):
    if n == 1:
        return 1
    else:
        return (josephus(n - 1, m) + m - 1) % n + 1

while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break
    print(josephus(n, m))