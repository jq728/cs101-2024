def arrange(numlst,path):
    if len(path)==len(numlst):
        print(*path)
        return
    for i in range(len(numlst)):
        if numlst[i]:
            para=numlst[i]
            numlst[i]=False
            path.append(para)
            arrange(numlst,path)
            numlst[i]=para
            path.pop()
n=int(input())
nums=[i for i in range (1,n+1)]
arrange(nums,[])