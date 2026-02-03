#write a program to perform all these tasks
# a.     Store a number in a variable
#
# b.    If value is not in range (100-1000) prints WRONG NUMBER else follows the steps
#
# c.     Check even or odd
#
# d.    If even divide the number by 3 and print the remainder
#
# e.     If odd divide the number by 2 and print the remainder.
# b=int(input())
# if 100<=b<=1000:
#     if(b%2==0):
#         a=b%3
#         print(a)
#     else:
#         c=b%2
#         print(c)
# else:
#     print("WRONG NUMBER")


#write a progrm to perform given tasks
# Declare & initialize a number.
#
# Check whether the number is in range 0-100 or not.
#
# If not in range print INVALID INPUT
#
# Else – if the number is in range 91-100 then print SUPER SMART,
#
# 81-90 print SMART,
#
# 71-80 print SMART ENOUGH,
#
# 61-70 print JUST SMART,
#
# 36-60 print NO SMART,
#
# 0-35 print DUMB.
a=int(input())
# if 0<=a<=100:
#     if 91<=a<=100:
#         print("SUPER SMART")
#     elif 81<=a<=90:
#         print("SMART")
#     elif 71<=a<=80:
#         print("SMART ENOUGH")
#     elif 61<=a<=70:
#         print("JUST SMART")
#     elif 36<=a<=60:
#         print("NO SMART")
#     elif 0<=a<=35:
#         print("DUMB")
# else:
#     print("INVALID INPUT")

#write a program to convert kg values into gram values?
# kg=float(input())
# g=int(kg*1000)
# print("%d Grams"%g)

#Write a program to find sum of all the numbers in given range if starting
# # index is greater than ending index print INVALID RANGE
# a=int(input())
# b=int(input())
# if(a>b):
#     print("INVALID RANGE")
# else:
#     sum=0
#     for i in range(a,b+1):
#         sum=sum+i
#     print(sum)

# #Write a program to print CVCORP for 'N' times
# a=int(input())
# if 10<a<100:
#     c="CVCORP\n"*a
#     print(c)
# else:
#     print("Invalid Input")

#Write a program to convert temperature from degree celcisu (C)
# to Farenheit (F).
# a=int(input())
# f=(a*9/5)+32
# print(F"{f}F")

#Write a program to print all numbers which are divisible by 11 in
# given range if no such numbers print NO NUMBERS if starting range
# is greater than ending range then print INVALID RANGE
# a=int(input())
# b=int(input())
# n=0
# if a>b:
#     print("INVALID RANGE")
# else:
#     for i in range (a,b+1):
#         if i%11==0:
#             print(i,end=" ")
#             n+=1
#     if n==0:
#         print("NO NUMBERS")


# Write a program to print all even numbers in range .if starting range
# is greater than ending range print "INVALID RANGE"
# a=int(input())
# b=int(input())
# if a>b:
#     print("INVALID RANGE")
# for i in range(a,b+1):
#     if i%2==0:
#         print(i,end=" ")


#Write a program to perform Addition, Subtraction, Multiplication and
# Division of 2 Numbers based on the user inputs by using Switch
# condition.(+ , - , * , /, %).
# a=int(input())
# b=int(input())
# i=input()
# if i=="+":
#     print(a+b)
# elif i=="-":
#     print(a-b)
# elif i=="*":
#     print(a*b)
# elif i=="//":
#     print(a//b)

#Write a Program to Print the Biggest Number out of the Given three
# Numbers?
# a=int(input())
# b=int(input())
# c=int(input())
# if a>b and a>c:
#     print(f"{a} is a Biggest Number from the Given Numbers")
# elif b>c:
#     print(f"{b} is a Biggest Number from the Given Numbers")
# else:
#     print(f"{c} is a Biggest Number from the Given Numbers")

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

#Input 1  :    10
# Output 1:    1, 2, factor of three, 4, 5, factor of three, 7, 8,
# factor of three, 10

# Input 2  :    24
# Output 2:    1, 2, factor of three, 4, 5, factor of three, 7, 8,
# factor of three, 10, 11, factor of three, 13, 14, factor of three,
# 16, 17, factor of three, 19, 20, factor of three, 22, 23, factor of
# three

#a=int(input())
# first =True
# for i in range(1,a+1):
#     if not first:
#         print(",",end=" ")
#     first= False
#     if(i%3==0):
#         print("factor of three",end="")
#     else:
#         print(i,end="")


# #Input 1  :    10
#                31
# Output 1:    10^2, 12^2, 14^2, 16^2, 18^2, 20^2, 22^2, 24^2, 26^2,
# 28^2, 30^2
#
# Input 2  :    -6
#                8
# Output 2:     Invalid Inputs
#
# Input 3  :    5
#               27
# Output 3:    5^2, 7^2, 9^2, 11^2, 13^2, 15^2, 17^2, 19^2, 21^2, 23^2,
# 25^2, 27^2

# a = int(input())
# b = int(input())
# c = 0
# if a > 0 and b > 0:
#     for i in range(a, b + 1, 2):
#         c = c + 1
#         if c > 1:
#             print(end=", ")
#         print(f"{i}^2", end="")
#
# else:
#     print("Invalid Inputs")


# Input 1: 10.7
#          12.1
# Output 1:
# 10.7 ^ 2, 10.9 ^ 2, 11.1 ^ 2, 11.3 ^ 2, 11.5 ^ 2, 11.7 ^ 2, 11.9 ^ 2,
# 12.1 ^ 2.
#
# Input 2: 6.1
#          8.9
# Output
# 2: 6.1 ^ 2, (6.3 ^ 2, 6.5 ^ 2, 6.7 ^ 2, 6.9 ^ 2, 7.1 ^ 2, 7.3 ^ 2,
# 7.5 ^ 2, 7.7 ^ 2, 7.9 ^ 2, 8.1 ^ 2, 8.3 ^ 2, 8.5 ^ 2, 8.7 ^ 2, 8.9 ^ 2.

# a=float(input())
# b=float(input())
# i=a
# while i<=b:
#         print(f"{i:.1f}^2",end="")
#         if round(i+0.2,1)<=b:
#             print(", ",end="")
#         else:
#             print(".")
#         i= round(i+0.2,1)


# Input 1: 10
#         -12
#
# Output 1:
#50, 45, 40, 35, 30, 25, 20, 15, 10, 5, 0, (-5), (-10), (-15), (-20),
# (-25), (-30), (-35), (-40), (-45), (-50), (-55), (-60)
#
# Input2: -6
#          8
# Output 2: (-30), (-25), (-20), (-15), (-10), (-5), 0, 5, 10, 15,
# 20, 25, 30, 35, 40

# n=int(input())
# n1=int(input())
# a=n*5
# b=n1*5
# count=0
# if a<=b:
#     for i in range(a,b+1,5):
#         if count>0:
#             print(", ",end="")
#         count+=1
#         if i<0:
#             print(f"({i})",end="")
#         else:
#             print(i,end="")
# else:
#     for i in range(a,b-1,-5):
#         if count>0:
#             print(", ",end="")
#         count+=1
#         if i<0:
#             print(f"({i})",end="")
#         else:
#             print(i,end="")


#Input 1  :    10
#              -12
# Output 1:
# 5*10, 5*9, 5*8, 5*7, 5*6, 5*5, 5*4, 5*3, 5*2, 5*1, 5*0, 5*(-1),
# 5*(-2), 5*(-3), 5*(-4), 5*(-5), 5*(-6), 5*(-7), 5*(-8), 5*(-9),
# 5*(-10), 5*(-11), 5*(-12)

# Input 2  :    -6
#                8
# Output 2: 5*(-6), 5*(-5), 5*(-4), 5*(-3), 5*(-2), 5*(-1), 5*0, 5*1,
# 5*2, 5*3, 5*4, 5*5, 5*6, 5*7, 5*8
#
#
# Input 3  : 5
#            8
# Output 3: 5*5, 5*6, 5*7, 5*8

# a=int(input())
# b=int(input())
# first= True
# if a>b:
#     step = -1
# else:
#     step= 1
# for i in range(a,b+step,step):
#     if not first:
#         print(", ",end="")
#     first = False
#     if i>=0:
#         print(f"5*{i}",end="")
#     else:
#         print(f"5*({i})",end="")

# Input :10
#        -5
# Output :10@9,(9@8,8@7,7@6,6@5,5@4,4@3,3@2,2@1,1@0,0@-1,
#         -1@-2,-2@-3,-3@-4,-4@-5,-5@-6)

# a=int(input())
# b=int(input())
# if a>b:
#     for i in range(a,b-1,-1):
#         print(f"{i}@{i-1}",end="")
#         if i!=b:
#             print(",",end="")
# else:
#     for i in range(a,b+1):
#         print(f"{i}@{i+1}",end="")
#         if i!=b:
#             print(",",end="")


# Input 1: 25
# Output
# 1: 1, 3, divisible by five, 7, 9, 11, 13, divisible by
# five, 17, 19, 21, 23, divisible by five
#
# Input 2: 38
#
# Output
# 2: 1, 3, divisible by five, 7, 9, 11, 13, divisible by five,
# 17, 19, 21, 23, divisible by five,
# 27, 29, 31, 33, divisible by five, 37


# a=int(input())
# first= True
# for i in range(1,a+1):
#     if i%2!=0:
#         if not first:
#             print(", ",end="")
#         first=False
#         if i%5==0:
#             print("divisible by five",end="")
#         else:
#             print(i,end="")


# Input
# 1: 10
#
# Output
# 1: 5, 10, 5, 10, 5, 10, 5, 10, 5, 10
#
# Input
# 2: -6
#
# Output
# 2: Invalid
# Input
#
# Input
# 3: 5
#
# Output
# 3: 5, 10, 5, 10, 5

# n=int(input())
# if n<=0:
#     print("Invalid Input")
# else:
#     for i in range(n):
#         if i%2==0:
#             print(5,end="")
#         else:
#             print(10,end="")
#         if i!=n-1:
#             print(", ",end="")


# Input 1: 36
#
# Output
# 1: 1, even, 3, even, 5, even, 7, even, 9, even, 11, even, 13,
# even, 15, even, 17, even, 19, even, 21, even, 23, even, 25, even,
# 27, even, 29, even, 31, even, 33, even, 35, even
#
# Input 2: 9
#
# Output
# 2: 1, even, 3, even, 5, even, 7, even, 9
# n=int(input())
# for i in range (1,n+1):
#     if i%2==0:
#         print("even",end="")
#     else:
#         print(i,end="")
#     if i!=n:
#         print(", ",end="")


# Input 1: 100
# 1000
#
# Output 1: 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000
#
# Input 2: 300
# 2500
#
# Output 2: 300, (400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300,
# 1400, 1500, 1600, 1700, 1800, 1900, 2000, 2100, 2200, 2300, 2400, 2500

# a=int(input())
# b=int(input())
# first = True
# if a>0 and b>0:
#     for i in range(a,b+100,100):
#         if not first:
#             print(", ",end="")
#         first= False
#         print(i,end="")
# else:
#     print("Invalid Inputs")


#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>.
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#Write a Program to print the smallest digit in a Given Number?
# n=int(input())
# l=9
# if n<=0:
#     print("Invalid Input.")
# else:
#     while(n>0):
#         r=n%10
#         if r<l:
#             l=r
#         n=n//10
#     print(f"Smallest Digit in a Given Number is {l}.")

#Write a Program to print the Highest digit in a Given Number?
# n=int(input())
# h=0
# if n<=0:
#     print("Invalid Input.")
# else:
#     while(n>0):
#         r=n%10
#         if r>h:
#             h=r
#         n=n//10
#     print(f"Highest Digit in a Given Number is {h}.")



#Write a Program to Print Count no of Digits in a Given Number?
# a=int(input())
# c=0
# if a==0:
#     print("InvaliD Input")
# else:
#     if a<0:
#         a=-a
#         while(a>0):
#             a=a//10
#             c=c+1
#         if c==1:
#             print(f"Given Number consists of only {c} Digit and it is Negative Value." )
#         else:
#             print(f"Given Number consists of {c} Digits and it is Negative Value.")
#     else:
#         while a>0:
#             r=a%10
#             a=a//10
#             c=c+1
#         if c==1:
#             print(f"Given Number consists of only {c} Digit.")
#         else:
#             print(f"Given Number consists of {c} Digits.")


#Write a Program to check if the Given Number is Perfect Square or Not a perfect Square?
# n=int(input())
# from math import sqrt
# if n<=0:
#       print("InvaliD Input")
# else:
#     b=int(sqrt(n))
#     if b*b==n:
#         print("Given Number is a Perfect Square.")
#     else:
#         print("Given Number is Not a Perfect Square.")


#Write a Program to Print The Sum of the Even Digits in a Given Number?
# n=int(input())
# sum=0
# if n<=0:
#     print("Invalid Input")
# else:
#     while n>0:
#         r=n%10
#         if r%2==0:
#             sum=sum+r
#         n=n//10
#     print(sum)


#Write a program to find Sum of first 'n' Natural Numbers Without Using formula?
# n = int(input())
# sum = 0
# if n == 0:
#     print("InvaLid Input.")
# elif n < 0:
#     print(f"Sorry! you have Entered Negative Values.")
# else:
#     c = []
#     for i in range(1, n + 1):
#         sum = sum + i
#         if i < n:
#             c.append(i)
#         else:
#             c.append(i)
#
#     b = " + ".join(map(str, c))
#     print(f" Sum of 'N' Natural Numbers is {b} " + "= " + str(sum) + ".")



#Write a program to find Sum of first 'n' Natural Numbers by Using formula?
# n=int(input())
# if n==0:
#     print("InvaLid Input.")
# elif n<0:
#     print("Sorry! you have Entered Negative Values.")
# else:
#     d=n*(n+1)/2
#     e=int(d)
#     print(f"Sum of 'N' Natural Numbers is {e}.")


#Write a program to Find Sum of Digits of a Given Number?

# n=int(input())
# if n<=0:
#     print("Invalid Input.")
# else:
#     c=[]
#     while(n>0):
#         r=n%10
#         c.append(str(r))
#         n=n//10
#     c.reverse()
#     print(" + ".join(c),end=".")


#Write a Program to Print The Sum of all odd Positions in a Given Number?
# n=int(input())
# c=0
# sum=0
# if n<=0:
#     print("Invalid Input")
# else:
#     while n>0:
#         r=n%10
#         c=c+1
#         if c%2==1:
#             sum=sum+r
#         n=n//10
#     print(sum)




