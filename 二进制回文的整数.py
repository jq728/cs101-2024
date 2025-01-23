i=int(input())
a=bin(i)[2:]
b=a[::-1]
if a==b:
    print("Yes")
else:
    print("No")