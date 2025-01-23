m,n=map(int,input().split())
lst=[]
for k in range(0,n):
    k+= 1
    lst.append(k)
b=[]
for _ in range (m):
    a=list(map(int,input().split()))
    b.extend(a[1:])
c=list(set(sorted(b)))
if c==lst:
    print('YES')
else:
    print('NO')

