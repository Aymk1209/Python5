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
# cu=0
#
# for i in range(0,r):
#     for j in range(0,c):
#         if a[i][0]!=a[i][j]:
#             cu+=1
#             print("not eql")
#         if cu!=0:
#             break
# if cu==0:
#     print("eql row matrix")


# to check given matrix is equall collomun matrix or not
# r = int(input())
# c = int(input())
#
# a = []
# for i in range(r):
#     row = list(map(int, input().split()))
#     a.append(row)
# cu=0
#
# for i in range(0,c):
#     for j in range(0,r):
#         if a[0][i]!=a[j][i]:
#             cu+=1
#             print("not eql")
#         if cu!=0:
#             break
# if cu==0:
#     print("eql col matrix")






#matrix multiplication
# Matrix Multiplication

# r1 = int(input())
# c1 = int(input())
#
# a = []
# for i in range(r1):
#     row = list(map(int, input().split()))
#     a.append(row)
#
# r2 = int(input())
# c2 = int(input())
#
# b = []
# for i in range(r2):
#     row = list(map(int, input().split()))
#     b.append(row)
#
# if c1 != r2:
#     print("Matrix multiplication not possible")
# else:
#     for i in range(r1):
#         for j in range(c2):
#             s = 0
#             for k in range(c1):
#                 s += a[i][k] * b[k][j]
#             print(s, end=" ")
#         print()




#surroding elements
 #1. sum of surroding elements in a matrix
# r = int(input("Enter rows: "))
# c = int(input("Enter columns: "))
#
# a = []
#
# print("Enter matrix elements:")
# for i in range(r):
#     row = list(map(int, input().split()))
#     a.append(row)
#
# print("Element => Sum of surrounding elements")
#
# for i in range(r):
#     for j in range(c):
#         sum= 0
#         if i-1>=0:
#             sum+=a[i-1][j]
#         if j-1>=0:
#             sum+=a[i][j-1]
#         if j+1<c:
#             sum+=a[i][j+1]
#         if i+1<r:
#             sum+=a[i+1][j]
#         if i+1<r and j-1>=0:
#             sum+=a[i+1][j-1]
#         if i+1<r and j+1<c:
#             sum+=a[i+1][j+1]
#         if i-1>=0 and j+1<c:
#             sum+=a[i-1][j+1]
#         if i-1>=0 and j-1>=0:
#             sum+=a[i-1][j-1]
#         print(a[i][j],"->",sum)
#     print()





# d={1:10,
#    2:39,
#    3:67,
#    4:89,
#    5:67}
# print(sorted(d.items(),key=lambda x:x[1]))


# def merge(l:list[list[int]]):
#     l.sort(key=lambda x:x[1])
#     res=l[0]
#     for i in range(1,len(l)):
#         if res[-1][1]>l[i][0]:
#             res[-1][1]=max(res[-1][1],l[i][1])
#         else:
#             res.append(l[i])
#     return res
# l=list(map(int,input()))
# merge(l)







