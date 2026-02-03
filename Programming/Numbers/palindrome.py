#reveresing a given number
# n=int(input())
# sum=0
# while(n>0):
#     r=n%10
#     sum=sum*10+r
#     n=n//10
# print(sum)
from idlelib.macosx import readSystemPreferences

#given number is palindrome or not ?
# n=int(input())
# sum=0
# k=n
# while(n>0):
#     r=n%10
#     sum=sum*10+r
#     n=n//10
# if sum==k:
#     print("palindrome")
# else:
#     print("not a palindrome")

#in given range of numbers print palindrome numbers?

# n1=int(input())
# n2=int(input())
# for i in range(n1,n2+1):
#     l=i
#     rev=0
#     while(l>0):
#         r=l%10
#         rev=rev*10+r
#         l=l//n
#     if rev==i:
#         print(i)

#in given number we need to find highest digit?

# n=int(input())
# h=0
# while(n>0):
#     r=n%10
#     if r>h:
#         h=r
#     n=n//10
# print(h)

#in given number we need to find smallest digit?
# n=int(input())
# l=9
# while(n>0):
#     r=n%10
#     if r<l:
#         h=r
#     n=n//10
# print(l)


#highest number lowest number and diference b/w highest and lowest number
# n=int(input())
# h=0
# l=9
# while(n>0):
#     r=n%10
#     if r>h:
#         h=r
#     if r<l:
#         l=r
#     n=n//10
# print(h)
# print(l)
# num1=h
# num2=l
# result=num1-num2
# print(result)


#Write a program to print all Palindrome Numbers between the Given Numbers?
#
# a=int(input())
# b=int(input())
# if a<0 or b<0:
#     print("InvaliD InputS")
# else:
#     if a>b:
#         a,b=b,a
#     c=0
#     for i in range(a+1,b):
#         t=i
#         rev=0
#         while t>0:
#             r=t%10
#             rev=rev*10+r
#             t=t//10
#         if rev==i:
#             c=1
#             print(i,end="\n")
#     if c==0:
#         print("No Palindrome Values")


#Write a program to find Sum of all Palindrome Numbers between the Given Numbers?
# a=int(input())
# b=int(input())
# if a==0 or b==0:
#     print("INVALID Inputs")
# else:
#     if a<0:
#         a=-a
#     if b<0:
#         b=-b
#     if a>b:
#         a,b=b,a
#     c=True
#     sum=0
#     for i in range (a+1,b):
#         t=i
#         rev=0
#         while t>0:
#             r=t%10
#             rev=rev*10+r
#             t=t//10
#         if rev==i:
#             c=False
#             sum=sum+i
#     if c==True:
#         print("No Palindrome Values")
#     else:
#         print(sum)


#Write A Program to check the Given Number is Perfect Square or not?
#
# a=int(input())
# from math import sqrt
# if a<=0:
#     a=-a
# if a<=0:
#     print("Invalid Input")
# else:
#     b=int(sqrt(a))
#     if b*b==a:
#         print("Given Number is Perfect Square.")
#     else:
#         print("Given Number is Not a Perfect Square.")



#Write a program to find Average of all Palindrome Numbers between the Range?
# a=int(input())
# b=int(input())
# if a==0 or b==0:
#     print("INVALID Inputs")
# else:
#     if a<0:
#         a=-a
#     if b<0:
#         b=-b
#     if a>b:
#         print("Given Inputs are swapped")
#     else:
#         c=True
#         s=0
#         sum=0
#         for i in range(a,b+1):
#             t=i
#             rev=0
#             while t>0:
#                 r=t%10
#                 rev=rev*10+r
#                 t=t//10
#             if rev==i:
#                 c=False
#                 s=s+1
#                 sum=sum+i
#         if c==True:
#             print("No Palindrome Values")
#         else:
#             avg=sum/s
#             print(f"{avg:.2f}")


#Write a program to print Alternative Palindrome Numbers in the Given Range?
# a=int(input())
# b=int(input())
# if a<0 or b<0:
#     print("InvAlid InPUts")
# elif a>=0 and b>=0:
#     palindrome=[]
#     for i in range(a,b+1):
#         t=i
#         rev=0
#         while t>0:
#             r=t%10
#             rev=rev*10+r
#             t=t//10
#         if rev==i:
#             palindrome.append(i)
#     if len(palindrome)==0:
#         print("No Palindrome Values")
#     else:
#         alt=palindrome[::2]
#         print(", ".join(map(str,alt)),end=".")


#Write a program to Print the Reverse of a Given Number?
# a=int(input())
# if a<=0:
#     print("InValid Input")
# else:
#     rev=0
#     while a>0:
#         r=a%10
#         rev=rev*10+r
#         a=a//10
#     print(rev)

#Write a program to print the Sum of all Alternative Palindrome Numbers Between the Given Numbers?
# a=int(input())
# b=int(input())
# if a==0 or b==0:
#     print("Invalid Inputs")
# else:
#     if a<0:
#         a=-a
#     if b<0:
#         b=-b
#     if a>b:
#         a,b=b,a
#     palindrome=[]
#     c=0
#     sum=0
#     for i in range(a+1,b):
#         t=i
#         rev=0
#         while t>0:
#             r=t%10
#             rev=rev*10+r
#             t=t//10
#         if rev==i:
#             c=c+i
#             if c%2!=0:
#                 sum=sum+i
#                 palindrome.append(i)
#     if len(palindrome)==0:
#         print("No Palindrome Values")
#     else:
#         d=" + ".join(map(str,palindrome))
#         print(f"Sum of Alternative Palindrome Numbers between the {a} and {b} is {d} = {sum}.")


#Write a program to the check if the Given Number is a Palindrome or not and if it is a palindrome
# then Print PALINDROME, else Print the Reverse Value of a Given Number ?
# n=int(input())
# if n<0:
#     print("Invalid Input")
# elif n==0:
#     print("Zero")
# else:
#     i=n
#     rev=0
#     while i>0:
#         r=i%10
#         rev=rev*10+r
#         i=i//10
#     if rev==n:
#         print("Given Number is Palindrome")
#     else:
#         print(f"Reverse of a Given Number is {rev}")

# #factorial
# n=int(input())
# fact=1
# for i in  range (1,n+1):
#     fact=fact*i
# print(fact)

#


