#liner search
# l=list(map(int,input().split()))
# k=int(input())
# b=False
# for i in range(len(l)):
#     if k==l[i]:
#         b=True
#         break
# if b:
#     print("found")
# else:
#     print("not found")




#binary search
# l1 = list(map(int, input().split()))
# k=int(input())
# l1.sort()
# l,r=0,len(l1)-1
# b=False
# while(l<=r):
#     m=l+(r-1)//2
#     if l1[m]==k:
#         b=True
#         break
#     elif k>l1[m]:
#         l=m+1
#     else:
#         r=m-1
# if b:
#     print("found")
# else:
#     print("not found")


#whether to say the given list is in soreted order or not
# l = list(map(int, input().split()))
# b=True
# for i in range(len(l)-1):
#     if l[i]>l[i+1]:
#         b=False
#         break
# if b:
#     print("sorted")
# else:
#     print("not sorted")j