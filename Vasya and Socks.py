def socks(n, m):
    days = 0
    socks = n
    while socks > 0:
        days += 1
        if days % m == 0:
            socks += 1
        socks -= 1
    return days
n, m = map(int, input().split())
print(socks(n, m))