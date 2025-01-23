def wiggleMaxLength(nums):
    up = [1] * n
    down = [1] * n
    for i in range(1, n):
        if lst[i]>lst[i-1]:
            up[i] = max(up[i-1],down[i-1]+1)
        if lst[i]<lst[i-1]:
            down[i] = max(down[i-1],up[i-1]+1)
        if lst[i]==lst[i-1]:
            up[i] = up[i-1]
            down[i] = down[i-1]
    return max(max(up), max(down))
n=int(input())
lst=list(map(int,input().split()))
print(wiggleMaxLength(lst))