#finding the sub; sequences sets of the list
# l=[10,20,30,40]
# for i in range(1,2**len(l)):
#     ind=0
#     while i>0:
#         r=i%2
#         if r==1:
#             print(l[ind],end=" ")
#         ind=ind+1
#         i=i//2
#     print()



#if we give a number then if sum of any two numbers in list is equal
# l=[10,20,30,40]
# k=int(input())
# for i in range(1,2**len(l)):
#     ind=0
#     sum=0
#     l1=[]
#     while i>0:
#         r=i%2
#         if r==1:
#             sum=sum+l[ind]
#             l1.append(l[ind])
#             # print(l[ind],end=" ")
#         ind=ind+1
#         i=i//2
#     if sum==k:
#         print(*l1)