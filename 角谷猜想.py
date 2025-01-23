n=int(input())
while n != 1:
    if n%2==0:
        n = n//2
        print(f'{(n)*2}/2={n}')
    elif n%2!=0:
        n=n*3+1
        print(f'{((n)-1)//3}*3+1={n}')
if n==1:print('End')
