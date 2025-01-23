n=int(input())
result=''
for _ in range(n):
    str_ori=list(input())
    if len(str_ori)>10:
        result=f"{str_ori[0]}{len(str_ori)-2}{str_ori[-1]}"
        print(result)
    else:
        result=''.join(str_ori)
        print(result)