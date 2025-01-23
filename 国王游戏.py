n=int(input())
a,b=map(int,input().split())
l=[]
for _ in range(n):
    x,y=map(int,input().split())
    l.append((x,y))
from functools import cmp_to_key
def compare(a1, b1, a2, b2):
    return (max(1 / b1, a1 / b2) >= max(1 / b2, a2 / b1)) - \
           (max(1 / b1, a1 / b2) < max(1 / b2, a2 / b1))
def compare_wrapper(x, y):
    return compare(x[0], x[1], y[0], y[1])
l = sorted(l, key=cmp_to_key(compare_wrapper))
ans=a//l[0][1]
for i in range(1,n):
    a*=l[i-1][0]
    b*=l[i-1][1]
    ans=max(ans,a//l[i][1])
print(ans)