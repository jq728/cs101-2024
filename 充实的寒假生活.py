n=int(input())
lst=[]
for _ in range(n):
    begin,end=map(int,input().split())
    lst.append([begin,end])
lst.sort(key=lambda x:x[1])
count=1
last_end=lst[0][1]
for i in range(1,n):
    if lst[i][0]>last_end:
        count+=1
        last_end=lst[i][1]
print(count)