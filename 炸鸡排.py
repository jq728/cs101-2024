n,k=map(int,input().split())
t=list(map(int,input().split()))
s=0.0
for a in t:
    s+=a
t.sort(reverse=True)
for a in t:
    if a>s/k:
        s-=a
        k-=1
print("%.3f"%(s/k))