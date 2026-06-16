def solution(arr):
    n = len(arr)
    for i in range(0,n):
        max_index = i
        for j in range(i+1,n):
            if arr[max_index]>arr[j]:
                arr[max_index],arr[j]=arr[j],arr[max_index]
l=list(map(int,input().split()))
solution(l)
print(l)

