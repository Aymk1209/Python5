#digit count
# n=int(input())
# dc=0
# while(n>0):
#     dc=dc+1
#     n=n//10
# print(dc)

# print whether given number is amstrong or not?
# n=int(input())
# t=n
# dc=0
# sum=0
# while(t>0):
#     dc=dc+1
#     t=t//10
# t=n
# while(t>0):
#     r=t%10
#     sum=sum+(r**dc)
#     t=t//10
# if sum==n:
#     print(f"{n} is amstrong number")
# else:
#     print("not a amstrong number")
#
# Write a program to check if the Given Number is Armstrong or not?
# n=int(input())
# t=n
# dc=0
# sum=0
# if n<=0:
#     print("Invalid Input")
# else:
#     while t>0:
#         dc=dc+1
#         t=t//10
#     t=n
#     while t>0:
#         r=t%10
#         sum=sum+(r**dc)
#         t=t//10
#     if sum==n:
#         print("Armstrong Number")
#     else:
#         print("Not a Armstrong Number")



#Write a program to print the Armstrong Numbers in the Given Range.
# n1=int(input())
# n2=int(input())
# if n1>n2:
#     n1,n2=n2,n1
# if n1<=0 or n2<=0:
#     print("Invalid Inputs")
# else:
#     res=[]
#     for num in range (n1,n2+1):
#         t=num
#         dc=0
#         arm=0
#         while t>0:
#             dc=dc+1
#             t=t//10
#         t=num
#         while(t>0):
#             r=t%10
#             arm=arm+(r**dc)
#             t=t//10
#         if arm==num:
#            res.append(num)
#     if len(res):
#         print("Armstrong Numbers in the Given Range is ",end="")
#         print(", ".join(map(str,res)), end=".")
#     else:
#         print("No Armstrong Numbers")


#Write a program to print the Armstrong Numbers between the Given
# two values.
# n1=int(input())
# n2=int(input())
# if n1<0:
#     n1=-n1
# if n2<0:
#     n2=-n2
# if n1>n2:
#     n1,n2=n2,n1
# if n1==0 or n2==0:
#     print("Invalid Inputs")
# else:
#     res=[]
#     for num in range(n1+1,n2):
#         t=num
#         dc=0
#         arm=0
#         while t>0:
#             dc=dc+1
#             t=t//10
#         t=num
#         while t>0:
#             r=t%10
#             arm=arm+r**dc
#             t=t//10
#         if arm==num:
#             res.append(num)
#     if len(res):
#         print("Armstrong Numbers between the Given Values is ",end="")
#         print(", ".join(map(str,res)),end=".")
#     else:
#         print("No Armstrong Numbers Between Given Values")



#Write a program to print the Sum of the Armstrong Numbers in the
# Given Range?
# a=int(input())
# b=int(input())
# sum=0
# first=True
# found=True
# if a==0 or b==0:
#     print("Invalid Inputs")
# else:
#     if a<0 or b<0:
#         a=abs(a)
#         b=abs(b)
#     if a>b:
#         a,b=b,a
#     for i in range(a,b+1):
#         n=i
#         arm=0
#         dc=len(str(i))
#         while n>0:
#             r=n%10
#             arm=arm+(r**dc)
#             n=n//10
#         if arm==i:
#             sum=sum+arm
#             if first:
#                 print("Armstrong Numbers in the Given Range is",i,end="")
#                 first=False
#             else:
#                 print(" +",i,end="")
#     if sum==0:
#         print("No Armstrong Numbers in a Given Range.")
#     else:
#         print(" =",sum,end=".")


#Write a program to check Whether the Given Number
# (any number of digits) is Armstrong or Not
# n=int(input())
# n1=len(str(n))
# t=n
# arm=0
# if n<=0:
#     print("Invalid Input")
# else:
#     while t>0:
#         r=t%10
#         arm=arm+(r**n1)
#         t=t//10
#     if arm==n:
#         print(f"{n} is a Armstrong Number.")
#     else:
#         print(f"{n} is Not a Armstrong Number.")

#Write a program to print the Alternative Armstrong
# Numbers between the Given Values?
#n=int(input())
# n1=int(input())
# if n<0 or n1<0:
#     a=abs(n)
#     n1=abs(n1)
#
# c=0
# a1=0
# if n==0 or n1==0:
#     print("Invalid Inputs")
# else:
#     first=True
#     found=True
#
#     if n>n1:
#         n,n1=n1,n
#     for i in range(n+1,n1):
#         t=i
#         arm=0
#         dc=len(str(i))
#         while t>0:
#             r=t%10
#             arm=arm+(r**dc)
#             t=t//10
#         if arm==i:
#             c=c+1
#             if c%2==1:
#                 if first:
#                     a1=a1+1
#                     print("Alternative Armstrong Numbers between the Given Values is",arm,end="")
#                     first=False
#                 else:
#                     print(",",arm,end="")
#     if a1==0:
#         print("No Armstrong Numbers Between Given Values.")
#     else:
#         print(".")



#