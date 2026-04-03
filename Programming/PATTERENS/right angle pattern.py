# *
#
# **
#
# ***
#
# ****
#
# *****

# n=int(input())
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print("*",end=" ")
#     print()




#     *
#
#    **
#
#   ***
#
#  ****
#
# *****
# n=int(input())
# for i in range(1,n+1):
#     print(" "*(n-i),end="")
#     for j in range(1,i+1):
#         print("*",end="")
#     print()



# @ @ @ @ @
#
# @ @ @ @
#
# @ @ @
#
# @ @
#
# @
# n=int(input())
# for i in range(n,0,-1):
#     for j in range(1,i+1):
#         print(end="@ ")
#     print()



# 1
#
# 1 2
#
# 1 2 3
#
# 1 2 3 4
#
# 1 2 3 4 5
#
# 1 2 3 4 5 6
# n=int(input())
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print()


#1
#
# 2 3
#
# 4 5 6
#
# 7 8 9 10
#
# 11 12 13 14 15

# n=int(input())
# num=1
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(num,end=" ")
#         num+=1
#     print()



#10 10 10 10 10

# 8 8 8 8
#
# 6 6 6
#
# 4 4
#
# 2
# n=int(input())
# num=n*2
# for i in range(n,0,-1):
#     for j in range(1,i+1):
#         print(num,end=" ")
#     num=num-2
#     print()


# *****
#
#  ****
#
#   ***
#
#    **
#
#     *

# n=int(input())
# for i in range(n,0,-1):
#     print(" "*(n-i),end="")
#     for j in range(i):
#         print("*",end="")
#     print()


# 100
#
# 200 300
#
# 400 500 600
#
# 700 800 900 1000
# n=int(input())
# num=100
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(num,end=" ")
#         num+=100
#     print()




# 5 4 3 2 1
#
# 4 3 2 1
#
# 3 2 1
#
# 2 1
#
# 1
# n=int(input())
# for i in range(n,0,-1):
#     print(" ",end="")
#     for j in range(i,0,-1):
#         print(j,end=" ")
#     print()





# 2
#
# 3 5
#
# 6 8 10
#
# 11 13 15 17
#
# 18 20 22 24 26

# n=int(input())
# num=2
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(num,end=" ")
#         if i==j:
#             num+=1
#         else:
#             num+=2
#     print()



# 1 2 3 4 5 6
#
# 5 4 3 2 1
#
# 1 2 3 4
#
# 3 2 1
#
# 1 2
#
# 1

# n=int(input())
# for i in range(n,0,-1):
#     if (n-i)%2==1:
#         for j in range(i,0,-1):
#             print(j,end=" ")
#         print()
#     else:
#         for j in range(1,i+1):
#             print(j,end=" ")
#         print()
#
#




#prime right angle triangle
# n=int(input())
# num=2
# for i in range(1,n+1):
#     c=0
#     while c<i:
#         prime=True
#
#         for j in range(2,num):
#             if num%j==0:
#                 prime=False
#                 break
#         if prime:
#             print(num,end=" ")
#             c+=1
#         num+=1
#     print()







#fibonacii right angle triangle
# n=int(input())
# a=0
# b=1
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(a,end=" ")
#         c=a+b
#         a=b
#         b=c
#     print()


#mixed pattern of prime in fibb
# n=int(input())
# a=0
# b=1
# num=2
# for i in range(1,n+2):
#     for j in range(1,i+1):
#         if j%2==1:
#             print(a,end=" ")
#             c=a+b
#             a=b
#             b=c
#         else:
#             print(num,end=" ")
#             num+=1
#     print()




#prime+fibb alternating triangle
# n=int(input())
# if n<=0:
#     print("Invalid ")
# else:
#     prime=2
#     a=0
#     b=1
#     c=1
#     for i in range(1,n+1):
#         for j in range(1,i+1):
#             if c%2==1:
#                 while True:
#                     is_prime=True
#                     for k in range(2,prime):
#                         if prime%k==0:
#                             is_prime=False
#                             break
#                     if is_prime:
#                         print(prime,end=" ")
#                         prime+=1
#                         break
#                     prime+=1
#             else:
#                 print(a,end=" ")
#                 c=a+b
#                 a=b
#                 b=c
#             c+=1
#         print()




n=int(input())
if n<=0:
    print("Invalid Input")
else:
    for i in range(n,0,-1):
        print(" "*(n-i),end="")
        for j in range(i,0,-1):
            print("*",end=" ")
        print("  "*(n-i),end="")
        for j in range(i,0,-1):
            print("*",end=" ")
        print()
    for i in range(2,n+1):
        print(" "*(n-i),end="")
        for j in range(1,i+1):
            print("*",end=" ")
        print("  "*(n-i),end="")
        for j in range(1,i+1):
            print("*",end=" ")
        print()