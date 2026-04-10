#Write a program to print all possible sublists of a list.
# l=[10,20,30,40]
# for i in range(len(l)):
#     for j in range(i,len(l)):
#         for k in range(i,j+1):
#             print(l[k],end=" ")
#         print()


               #OR
# l=[10,20,30,40]
# for i in range(len(l)):
#     for j in range(i, len(l)):
#         l1=l[i:j+1]
#         print(*l1)



#if a number is given then sum of 2 num's present in list print them
# l=[10,20,30,40]
# k=int(input())
# for i in range(len(l)):
#     for j in range(i, len(l)):
#         l1=l[i:j+1]
#         if(sum(l1)==k):
#             print(*l1)

#if a number is given then that many elements in list should be print , kth time elemnts
# l=[10,20,30,40,50,60]
# k=int(input())
# if k>len(l):
#     print("out of range")
# else:
#     l1=l[0:k]
#     print(*l1)


# l=[10,20,30,40,50,60]
# k=int(input())
# for i in range(len(l)):
#     for j in range(i,len(l)):
#         l1=l[i:j+1]
#         l2=len(l1)
#         if k==l2:
#             print(*l1,end=" ")
#             print()
