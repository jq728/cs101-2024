n = int(input())
m = set(range(1, n + 1))
kid = [int(a) for a in input().split()]
lost = []

for i in range(len(kid) - 1, -1, -1):  # 从后往前遍历，避免索引问题
    if kid[i] not in m:
        lost.append(kid[i])
        kid.pop(i)
kid_1=[x for x in m if x not in kid]
k=map(str,sorted(kid_1))
l=map(str,sorted(lost))
print(' '.join(k))
print(' '.join(l))
