for _ in range(int(input())):
    n, m, b = map(int, input().split())
    s = {}
    ts = []
    for _ in range(n):
        t, x = map(int, input().split())
        if t in s:
            s[t].append(x)
        else:
            s[t] = [x]
            ts.append(t)
    ts.sort()
    for t in ts:
        d = sum(sorted(s[t], reverse=True)[:m])
        b -= d
        if b <= 0:
            print(t)
            break
    if b > 0:
        print("alive")