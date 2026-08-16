# l=8,2,25,16,20,39,4,15
#start<end then only we can sort the array
# def split(l,s,e):
#     p=s
#     i=s+1
#     j=e
#     while True:
#
#         while i<=e and l[i]<=l[p]:
#             i+=1
#         while j>=s and l[j]>l[p]:
#             j-=1
#         if i<j:
#             l[i],l[j]=l[j],l[i]
#         else:
#             l[p], l[j] = l[j], l[p]
#             break
#
#     return j
#
# def quicksort(l,s,e):
#     if s<e:
#         j=split(l,s,e)
#         quicksort(l,s,j-1)
#         quicksort(l,j+1,e)
# l=list(map(int,input().split()))
# quicksort(l,0,len(l)-1)
# print(l)
