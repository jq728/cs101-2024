n = int(input())
for _ in range(n):
    id_number = input().strip()
    coefficients = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
    check_codes = ['1', '0', 'X', '9', '8', '7', '6', '5', '4', '3', '2']
    sum_product = sum(int(num) * coef for num, coef in zip(id_number[:-1], coefficients))
    remainder = sum_product % 11
    print("YES" if id_number[-1].upper() == check_codes[remainder] else "NO")