def find_next_peak(p, e, i, d):
    cycle_p = 23
    cycle_e = 28
    cycle_i = 33
    x = 0
    for t in range(d + 1, d+21253):
        if t % cycle_p == p % cycle_p and t % cycle_e == e % cycle_e and t % cycle_i == i % cycle_i:
            x = t
            break
    return x - d

num=1
while True:
    p, e, i, d = map(int, input().split())
    if p == e == i == d == -1:
        break
    print(f"Case {num}: the next triple peak occurs in {find_next_peak(p, e, i, d)} days.")
    num+=1