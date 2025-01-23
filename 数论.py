def M(n):
    if n == 1:
        return 1
    lst = []
    seen = set()
    for i in range(2, int(n**0.5) + 1):
        while n % i == 0:
            if i in seen:
                return 0
            seen.add(i)
            n //= i
    if n > 1:
        if n in seen:
            return 0
        seen.add(n)
    if len(seen) % 2 == 0:
        return 1
    else:
        return -1

n = int(input())
print(M(n))
