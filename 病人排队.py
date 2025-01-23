n=int(input())
p=[]
for i in range(n):
    id,age=input().split()
    age=int(age)
    p.append((id,age,i))
p.sort(key=lambda p:(-p[1],p[2]) if p[1]>=60 else (p[2],))
for ppl in p:
    print(ppl[0])