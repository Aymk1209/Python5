def solution(l):
    for i in range (0,len(l)-1):
        for j in range(i+1,len(l)):
            if l[i]>l[j]:
                l[i],l[j]=l[j],l[i]
l=list(map(int,input().split()))
solution(l)
print(l)