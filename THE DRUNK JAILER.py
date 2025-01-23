n=int(input())
for _ in range(n):
    jail=int(input())
    c=0
    for i in range(1,jail+1,2):
        if ((1+i)*(i+1)/2)/2<=jail:
            c+=1
    print(c)