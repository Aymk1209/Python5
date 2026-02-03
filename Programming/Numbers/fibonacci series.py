#n fibonacci series
# n=int(input())
# a=0
# b=1
# for i in range(1,n+1):
#     print(a)
#     c=a+b
#     a=b
#     b=c

#sum of n fibonacci series
# n=int(input())
# a=0
# b=1
# sum=0
# for i in range(1,n+1):
#     sum=sum+a
#     c=a+b
#     a=b
#     b=c
# print(sum)


#avg of all fibonacci series
# n= int(input())
# a=0
# b=1
# sum=0
# for i in range(1,n+1):
#     sum=sum+a
#     c=a+b
#     a=b
#     b=c
# avg=sum//n
# print("%.2f" %avg)

# #alternative ficcbonic series
# n=int(input())
# a=0
# b=1
# for i in range(1,n+1):
#     if(i%2==1):
#         print(a)
#     c=a+b
#     a=b
#     b=c


#Write a program to find Factorial of a Given Number?
# n=int(input())
# fact=1
# if n<0:
#     print("Invalid InPut")
# else:
#     for i in range(1,n+1):
#         fact=fact*i
#     print(fact)

# First Line of Input Consists of One Integer
#n=int(input())
# a=0
# b=1
# if n<=0:
#     print("Invalid Input")
# else:
#     sum=0
#     for i in range(1,n+1):
#         sum=sum+a
#         c=a+b
#         a=b
#         b=c
#     print(sum)


#Write a program to print First N terms in the Fibonacci Series?
# n=int(input())
# a=0
# b=1
# if n<0:
#     n=-n
# if n==0:
#     print("Invalid Input")
# else:
#     for i in range(1,n+1):
#         print(a,end=" ")
#         c=a+b
#         a=b
#         b=c


#Write a program to print Fibonacci Series in the Given Range.
# n1 = int(input())
# n2 = int(input())
# a = 0
# b = 1
# d = 0
# if n1 < 0 or n2 < 0:
#     print("Invalid Inputs")
# else:
#     if n1 > n2:
#         n1, n2 = n2, n1
#     while (a <= n2):
#
#         if a >= n1:
#             d = d + 1
#             print(a, end=" ")
#
#         c = a + b
#         a = b
#         b = c
#     if d == 0:
#         print("No Fibonacci Series Values")


#Write a program to print the Average of the
# Fibonacci Series in Between the Given Range?
# n1 = int(input())
# n2 = int(input())
# a = 0
# b = 1
# d = 0
# sum = 0
# if n1 < 0 or n2 < 0:
#     print("Invalid Inputs")
# else:
#     if n1 > n2:
#         n1, n2 = n2, n1
#     while (a <= n2):
#         if a >= n1:
#             d = d + 1
#             sum = sum + a
#         c = a + b
#         a = b
#         b = c
#     if d != 0:
#         avg = sum / d
#         print(f"{avg:.2f}")
#
#     if d == 0:
#         print("No Fibonacci Series Values")


#Write a program to print the Average of the
# Alternative Fibonacci Series in the Given Range?
# n1 = int(input())
# n2 = int(input())
# a = 0
# b = 1
# d = 0
# s = 0
# sum = 0
# if n1 < 0 or n2 < 0:
#     print("Invalid Inputs")
# else:
#     if n1 > n2:
#         n1, n2 = n2, n1
#     while (a <= n2):
#         if a >= n1:
#             s = s + 1
#             if s % 2 == 1:
#                 d = d + 1
#                 sum = sum + a
#
#         c = a + b
#         a = b
#         b = c
#     if d != 0:
#         avg = sum / d
#         print(f"{avg:.2f}")
#     if d == 0:
#         print("No Fibonacci Series Values")

# #Write a program to print First N terms of Alternative Fibonacci Series?
# n=int(input())
# a=0
# b=1
# result=[]
# if n<0:
#     n=-n
# if n==0:
#     print("Invalid Input")
# else:
#     for i in range(1,n*2):
#         if (i%2==1):
#             result.append(str(a))
#         c=a+b
#         a=b
#         b=c
#     print(", ".join(result))


#Write a program to find sum of Factorials upto
# N Numbers like 0! + 1! + 2! + 3! + 4! + 5! +....upto n!?
# n=int(input())
# if n<0:
#     print("INvalid INput")
# else:
#     fact=1
#     sum=0
#     list=[]
#     for i in range (n+1):
#         if i==0 or i==1:
#             fact=1
#         else:
#             fact=fact*i
#         sum=sum+fact
#         list.append(str(fact))
#     print(f"+".join (list) + "=" + str(sum))