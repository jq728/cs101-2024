def generate_lucky_numbers(lim):
    lucky_numbers = []
    for i in range(1, lim + 1):
        if all(c in {'4', '7'} for c in str(i)):
            lucky_numbers.append(i)
    return lucky_numbers

n = int(input())
lucky_numbers = generate_lucky_numbers(1000)
is_almost_lucky = any(n % lucky == 0 for lucky in lucky_numbers)
print("YES" if is_almost_lucky else "NO")