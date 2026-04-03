#anticlockwise
# Write a program to print all rotations of a list (anticlockwise)
# l=[10,20,30,40]
# for i in range(len(l)):
#     print(*l)
#     l=l[1: ]+[l[0]]
      #0r
# l=[10,20,30,40]
# for i in range(len(l)):
#     print(*l)
#     t=l[0]
#     for j in range(1,len(l)):
#         l[j-1] =l[j]
#     l[len(l)-1]=t


#clockwise
#Write a program to print all rotations of a list (clockwise)
# l=[10,20,30,40]
# for i in range(len(l)):
#     print(*l)
#     l=[l[len(l)-1]]+l[0:len(l)-1]
        #or
# l=[10,20,30,40]
# for i in range(len(l)):
#     print(*l)
#     t=l[len(l)-1]
#     for j in range(len(l)-2,-1,-1):
#         l[j+1]=l[j]
#     l[0]=t



# Write a program to rotate a list by k positions.(clockwise)
# l=[10,20,30,40]
# k=int(input())
# for i in range(len(l)):
#     if k%len(l)==i:
#         print(*l)
#         t=l[len(l)-1]
#         for j in range(len(l)-2,-1,-1):
#             l[j+1]=l[j]
#         l[0]=t


# Write a program to rotate a list by k positions.(anticlockwise)
# l=[10,20,30,40]
# k=int(input())
# for i in range(len(l)):
#     if k%len(l)==i:
#         print(*l)
#         t=l[0]
#         for j in range(1,len(l)):
#             l[j-1] =l[j]
#         l[len(l)-1]=t