def min_moves(n):
    if n == 1:
        return 0
    elif n % 6 != 0 and n % 3 != 0:
        return -1
    else:
        moves = 0
        while n > 1:
            if n % 6 == 0:
                n //= 6
            elif n % 3 == 0:
                n *= 2
            else:
                return -1
            moves += 1
        return moves

t = int(input())
for _ in range(t):
    n = int(input())
    print(min_moves(n))