n=int(input())
n1=0
while n!=1:
    if n%2!=0:
        n1=n*3+1
        print(f'{n}*3+1={n1}')
        n=n1
    else:
        n1=n//2
        print(f'{n}/2={n1}')
        n=n1