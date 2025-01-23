def max_candy_value(n, W, candies):
    candy_ratios = []
    for value, weight in candies:
        if weight > 0:
            candy_ratios.append((value, weight, value / weight))
    candy_ratios.sort(key=lambda x: x[2], reverse=True)
    total_value = 0.0
    remaining_weight = W
    for value, weight, ratio in candy_ratios:
        if remaining_weight <= 0:
            break
        if weight <= remaining_weight:
            total_value += value
            remaining_weight -= weight
        else:
            total_value += ratio * remaining_weight
            remaining_weight = 0
    return total_value

n, W = map(int, input().strip().split())
candies = []
for _ in range(n):
    v, w = map(int, input().strip().split())
    candies.append((v, w))

max_value = max_candy_value(n, W, candies)

print(f"{max_value:.1f}")