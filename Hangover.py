def min_cards(c):
    n = 2
    total_overhang = 1/2
    while total_overhang < c:
        total_overhang += 1 / n
        n += 1
    return n

while True:
    c = float(input())
    if c == 0.00:
        break
    print(min_cards(c),"card(s)")