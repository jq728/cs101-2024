def calculate_sum(n):
    total_sum = n * (n + 1) // 2
    power_of_two_sum = 0
    power = 1
    while power <= n:
        power_of_two_sum += power
        power *= 2

    return total_sum - 2 * power_of_two_sum

t = int(input())
for _ in range(t):
    n = int(input())
    print(calculate_sum(n))