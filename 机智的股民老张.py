def maxvalue(a):
    minv=a[0]
    maxv=0
    for i in a:
        if i<minv:
            minv=i
        else:
            maxv=max(maxv,i-minv)
    return maxv
lst=list(map(int,input().split()))
print(maxvalue(lst))