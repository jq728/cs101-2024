def competition(a,v1,v2):
    i=0
    v1.sort()
    v2.sort()
    m,n=0,0
    k,l=a-1,a-1
    while m<=k:
        if v1[m]>v2[n]:
            i+=200
            m+=1
            n+=1
        elif v1[k]>v2[l]:
            i+=200
            k-=1
            l-=1
        else:
            if v1[m]<v2[l]:
                i-=200
            m+=1
            l-=1
    return i
while True:
    a=int(input())
    if a==0:
        break
    else:
        v1=list(map(int,input().split()))
        v2=list(map(int,input().split()))
        result=competition(a,v1,v2)
        print(result)