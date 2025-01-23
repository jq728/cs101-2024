d=int(input())
n=int(input())
rubbish=[]
for j in range(n):
    x,y,i=map(int,input().split())
    rubbish.append((x,y,i))
points=[]
for xi in range (0,1025):
    for yi in range (0,1025):
        ttl = 0
        for x,y,i in rubbish:
            if abs(xi-x)<=d and abs(yi-y)<=d:
                ttl+=i
        points.append(ttl)
boom=max(points)
print(points.count(boom),boom)