n=int(input())
numbers=[int(a) for a in input().split()]
k=int(input())
c=0
for i in range(len(numbers)):
    for j in range(i+1,len(numbers)):
        if numbers[i]+numbers[j]==k:
            c+=1
        else:
            c+=0
print(c)