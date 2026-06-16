def solution(arr):
    n=len(arr)
    for i in range(n):
        c=0
        for j in range(n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
                c+=1
        if c==0:
            break
arr=list(map(int,input().split()))
solution(arr)
print(arr)