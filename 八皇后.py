def dfs(s):
    for i in range(1, 9):
        flag = True
        for j in range(len(s)):
            if int(s[j]) == i or abs(len(s) - j) == abs(i - int(s[j])):
                flag = False
                break
        if flag:
            if len(s) == 7:
                ans.append(s + str(i))
            else:
                dfs(s + str(i))
ans = []
dfs('')
n = int(input())
for i in range(n):
    l = int(input())
    print(ans[l - 1])