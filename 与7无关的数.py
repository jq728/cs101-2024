def sum_of_squares(n):
    sum_squares = 0
    for i in range(1, n + 1):
        if '7' not in str(i) and i % 7 != 0:
            sum_squares += i ** 2
    return sum_squares

n = int(input())
print(sum_of_squares(n))