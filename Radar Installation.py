n,d=map(int,input().split())
case_num=1
while [n,d]!=[0,0]:
    spots=[[int(a) for a in input().split()] for _ in range(n)]
    case_num+=1
    if spots[1]<=0:
        print(f"Case {case_num}: -1")
        continue

