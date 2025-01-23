def Hanoi(x,a,b,c):
    if x==1:
        print(f"{a}->{c}")
        return
    Hanoi(x-1,a,c,b)
    print(f"{a}->{c}")
    Hanoi(x-1,b,a,c)
n=int(input())
print(pow(2,n)-1)
Hanoi(n,"A","B","C")