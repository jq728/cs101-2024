from itertools import permutations, product
def result(nums):
    for p in permutations(nums):
        for ops in product("+-", repeat=3):
            exp = f"{p[0]}{ops[0]}{p[1]}{ops[1]}{p[2]}{ops[2]}{p[3]}"
            try:
                if eval(exp) == 24:
                    return "YES"
            except ZeroDivisionError:
                continue
    return "NO"

m = int(input())
for _ in range(m):
    nums = list(map(int, input().split()))
    print(result(nums))