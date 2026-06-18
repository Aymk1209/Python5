# write a pro to take the dynamic inputs from user for a inner list and print even numbers from the inner list
# n = int(input())
# lst = []
# for i in range(n):
#     lst.append(int(input()))
# print("Even Numbers:")
# for num in lst:
#     if num % 2 == 0:
#         print(num, end=" ")
# print()


# write a pro to find out all the prime numbers in the given inner list
# n = int(input())
# lst = []
# for i in range(n):
#     lst.append(int(input()))
# for num in lst:
#     if num > 1:
#         prime = True
#         for i in range(2, int(num**0.5) + 1):
#             if num % i == 0:
#                 prime = False
#                 break
#         if prime:
#             print(num, end=" ")
# print()



# write a pro to find out max and 2nd max elements in given inner list
# n = int(input())
# lst = []
# for i in range(n):
#     lst.append(int(input()))
#     max1 = float('-inf')
#     max2 = float('-inf')
#
# for num in lst:
#     if num > max1:
#         max2 = max1
#         max1 = num
#     elif num > max2 and num != max1:
#         max2 = num
#
# print("Max Element:", max1)
# print("Second Max Element:", max2)




# to find out the sum of elements of each row separately











# to find out the sum of diagonal elements of inner list
# r = int(input("Enter size of matrix: "))
#
# a = []
# for i in range(r):
#     row = list(map(int, input().split()))
#     a.append(row)
#
# sum = 0
#
# for i in range(r):
#     sum += a[i][i]
#
# print("Sum of diagonal elements:", sum)









# to check given matrix is identity matrix or no
# r = int(input())
# a = []
#
# for i in range(r):
#     a.append(list(map(int,input().split())))
#
# c = 0
#
# for i in range(r):
#     for j in range(r):
#         if i == j and a[i][j] == 1:
#             c += 1
#         elif i != j and a[i][j] == 0:
#             c += 1
#
# if c == r * r:
#     print("Identity Matrix")
# else:
#     print("Not an Identity Matrix")





#to find the sum of both digonel elemts separeatly
# r = int(input())
# a = []
# d1= 0
# d2= 0
#
# for i in range(r):
#     a.append(list(map(int, input().split())))
#     d1+= a[i][i]
#     d2 += a[i][r - i - 1]
#
# print("Primary Diagonal Sum =", d1)
# print("Secondary Diagonal Sum =", d2)


#equal row matrix or not?
# r = int(input())
# c = int(input())
#
# a = []
# for i in range(r):
#     row = list(map(int, input().split()))
#     a.append(row)
# c=0
#
# for i in range(0,r):
#     for j in range(0,c):
#         if a[i][0]!=a[i][j]:
#             c+=1
#             print("not eql")
#         if c!=0:
#             break
# if c==0:
#     print("eql row matrix")


# to check given matrix is equall collomun matrix or not





