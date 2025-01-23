n=int(input())
a=list(map(int,input().split()))
index=[(value,index) for index,value in enumerate(a,start=1)]
a=sorted(a)
b=sorted(index)
new=[index for value,index in b]
new=' '.join(map(str,new))
print(new)
c=0
lst=[]
for i in range(len(a)-1):
    c+=a[i]
    lst.append(c)
print(lst)
print("%.2f"%(sum(lst)/n))