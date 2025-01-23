dots=list(map(int,input().split()))
lst=sorted(dots)
print(abs(lst[0]-lst[1])+abs(lst[2]-lst[1]))