n, m1, m2 = map(int, input().split())
A = {}
B = {}
C = {}
for _ in range(m1):
    x, y, v = map(int, input().split())
    A[(x, y)] = v
for _ in range(m2):
    x, y, v = map(int, input().split())
    B[(x, y)] = v

for i in range(n):
    for k in range(n):
        s = sum(A.get((i, j), 0)*B.get((j, k), 0) for j in range(n))
        if s != 0:
            C[(i, k)] = s

ans = sorted(((k[0], k[1], v) for k, v in C.items()))
for x in ans:
    print(*x)