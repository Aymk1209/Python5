#Prime Number
# n=int(input())
# c=0
# if n<=0:
#     print("Invalid Input")
# else:
#     for i in range (1,n+1):
#         if n%i==0:
#             c=c+1
#     if(c==2):
#         print("Prime Number")
#     else:
#         print("Not a Prime Number")

# Prime Numbers in The Given Range
# n1=int(input())
# n2=int(input())
# c=0
# if n1>0 and n2>0:
#     for i in range(n1,n2+1):
#         fc=0
#         for j in range (1,i+1):
#             if i%j==0:
#                 fc=fc+1
#         if (fc==2):
#             c=c+1
#             if c>1:
#                 print(end=", ")
#             print(j,end="")
# else:
#     print("Invalid Inputs")


#Alternative Prime Numbers In the Given Range
# n1=int(input())
# n2=int(input())
# alt=0
# c=0
# if n1>0 and n2>0:
#     for i in range(n1,n2+1):
#         fc=0
#         for j in range (1,i+1):
#             if (i%j==0):
#                 fc=fc+1
#         if (fc==2):
#             c=c+1
#             alt=alt+1
#             if alt%2==1:
#                 if c>1:
#                     print(end=", ")
#                 print(j,end="")
# else:
#     print("Invalid Inputs")


# All Factors of The Given Number
# n = int(input())
# if n < 0:
#     print("Invalid Input")
# else:
#     for i in range(1, n + 1):
#         if n % i == 0:
#             print(i, end=" ")

# #Sum of all Alternative Prime Numbers Between The Given Values
# n1 = int(input())
# n2 = int(input())
# alt = 0
# sum = 0
# if n1 > 0 and n2 > 0:
#     for i in range(n1 + 1, n2):
#         fc = 0
#         for j in range(1, i + 1):
#             if i % j == 0:
#                 fc = fc + 1
#         if (fc == 2):
#             alt = alt + 1
#             if alt % 2 == 1:
#                 sum = sum + i
#     if sum == 0:
#         print("No Prime Numbers")
#     else:
#         print(sum)
#
# else:
#     print("Invalid Inputs")

#sum of all prime numbers
# n1=int(input())
# n2=int(input())
# sum=0
# for i in range(n1,n2+1):
#     fc=0
#     for j in range(1,i+1):
#         if(i%j==0):
#             fc=fc+1
#     if (fc==2):
#         sum=sum+i
# print(sum)

#print alternative prime numbers
# n1=int(input())
# n2=int(input())
# alt=0
# if n1>0 and n2>0:
#     for i in range(n1,n2+1):
#         fc=0
#         for j in range(1,i+1):
#             if(i%j==0):
#                 fc=fc+1
#         if (fc==2):
#             alt=alt+1
#             if (alt%2==1):
#                 print(i)
# else:
#     print("Invalid Inputs")

#finding
# from math import sqrt
# n=int(input())
# fc=0
# for i in range(2,int(sqrt(n))+1):
#     if n%i==0:
#         fc=fc+1
# if fc==0:
#     print("prime")
# else:
#     print("not prime")


#print prime number with out using factor count
# from math import sqrt
# n=int(input())
# b=True
# for i in range(2,int(sqrt(n))+1):
#     if n%i==0:
#         b=False
#         break
# if b==True and n>1:
#     print("prime")
# else:
#     print("not prime")


# #prime number without factor count
# n=int(input())
# b=True
# if n<1:
#     print("Invalid Input")
# else:
#     for i in range(2,n):
#         if n%i==0:
#             b=False
#             break
#     if (b):
#         print("Prime Number")
#     else:
#         print("Not a Prime Number")

#Sum of all The Primes Numbers Between The Given Values
# n1=int(input())
# n2=int(input())
# sum=0
# if n1>0 and n2>0:
#     for i in range(n1+1,n2):
#         fc=0
#         for j in range(1,i+1):
#             if (i%j==0):
#                 fc=fc+1
#         if (fc==2):
#             sum=sum+i
#     print(sum)
# else:
#     print("Invalid Inputs")


#Alternative Prime Numbers In the Given Range
# n1=int(input())
# n2=int(input())
# alt=0
# c=0
# if n1>0 and n2>0:
#     for i in range(n1,n2+1):
#         fc=0
#         for j in range (1,i+1):
#             if (i%j==0):
#                 fc=fc+1
#         if (fc==2):
#             c=c+1
#             alt=alt+1
#             if alt%2==1:
#                 if c>1:
#                     print(end=", ")
#                 print(j,end="")
# else:
#     print("Invalid Inputs")


#Write a program to print all Prime Factors of a Given Number?
# a=int(input())
# if a<0:
#     a=-a
# if a==0:
#     print("Invalid Input")
# elif a>=0:
#     for i in range (1,a+1):
#         if a%i==0:
#             fc=0
#             for j in range(1,i+1):
#                 if i%j==0:
#                     fc=fc+1
#             if fc==2:
#                 print(i,end=" ")
# else:
#     print("No Prime Factors")



#Write a Program to print the first 50 prime Numbers without using Factors count?
# from math import sqrt
# a=int(input())
# count =0
# num=2
# if(a<=0):
#     print("Invalid Input")
# else:
#     while(count < a ):
#         prime= True
#         for i in range(2,int(sqrt(num))+1):
#             if(num%i==0):
#                 prime=False
#                 break
#         if(prime):
#             if(count>0):
#                 print(end=", ")
#             print(num,end="")
#             count+=1
#         num+=1