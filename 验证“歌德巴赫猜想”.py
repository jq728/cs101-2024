def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

x = int(input())
if x < 6 or x % 2 != 0:
    print('Error!')
else:
    for y in range(2, x // 2 + 1):
        z = x - y
        if is_prime(y) and is_prime(z):
            print(f"{x}={y}+{z}")