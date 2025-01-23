def calculate_value(x):
    result=0
    for char in x:
        if '++' in char:
            result+=1
        elif '--' in char:
            result-=1
    return result

n = int(input())
x = []
for i in range(n):
    i=input()
    x.append(i)
print(calculate_value(x))
