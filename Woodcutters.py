n = int(input())
trees = [[int(a) for a in input().split()] for _ in range(n)]
count = 1
r = -trees[0][1]
for i in range(n-1):
    if trees[i][0]-trees[i][1] > r:
        count += 1
        r = trees[i][0]
    elif trees[i][0]+trees[i][1] < trees[i+1][0]:
        count += 1
        r = trees[i][0]+trees[i][1]
    else:
        r = trees[i][0]
print(count)