n = int(input())
forces = []
total_1=0
total_2=0
total_3=0
for _ in range(n):
    forces=[int(i) for i in input().split()]
    total_1 += forces[0]
    total_2 += forces[1]
    total_3 += forces[2]

if total_1 == total_2 == total_3 == 0:
    print("YES")
else:
    print("NO")