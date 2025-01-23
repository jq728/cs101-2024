while True:
    a,b = map(int,input().split())
    if a == b == 0:
        break
    if b > a:
        a,b = b,a
    if a >= (5**0.5+1)/2*b or a == b:
        print('win')
    else:
        print('lose')