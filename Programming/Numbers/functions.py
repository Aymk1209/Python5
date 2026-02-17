#using functions even or odd
# def isEvenOdd(a):
#     if a%2==0:
#         print("Even")
#     else:
#         print("odd")
# a=9
# isEvenOdd(a)
#
# #to return value
# def isevenodd(a):
#     if a%2==0:
#         return "even"
#     else:
#         return "odd"
# a=9
# k=isevenodd(a)
# print(k)
#OR
# def isevenodd(a):
#     if a%2==0:
#         return "even"
#     else:
#         return "odd"
# a=9
# print(isevenodd(a))


#for range of values even odd
# def iseven(n):
#     return n % 2 == 0
#
# def print_even(a, b):
#     for i in range(a, b):
#         if iseven(i):
#             print(i)
#
# a = 8
# b = 18
# print_even(a, b)



#for range of values sum of even
# def iseven(n):
#     return n%2==0
# def even(a, b):
#     sum=0
#     for i in range(a,b):
#         if iseven(i):
#             sum=sum+i
#     return sum
# a=8
# b=18
# print(even(a,b))


#for range of values avg of even
# def iseven(n):
#     return n%2==0
# def even(a,b):
#     sum=0
#     c=0
#     for i in range(a,b):
#         if iseven(i):
#             c=c+1
#             sum=sum+i
#     return sum/c
# a=8
# b=18
# print(even(a,b))


#****prime using funtions ****
# def prime(a):
#     fc=0
#     for i in range(1,a+1):
#         if a%i==0:
#             fc=fc+1
#     if fc==2:
#         print("prime")
#     else:
#         print("not prime")
# a=30
# print(prime(a))

#   OR

# def prime(a):
#     fc=0
#     for i in range(1,a+1):
#         if a%i==0:
#             fc=fc+1
#     return fc
# a=18
# k=prime(a)
# if k==2:
#     print("prime")
# else:
#     print("not prime")


#using boolen
# def prime(a):
#     fc=0
#     for i in range(1,a+1):
#         if a%i==0:
#             fc=fc+1
#     return fc==2
# a=18
# k=prime(a)
# if k:
#     print("prime")
# else:
#     print("nat prime")



#for range of numbers
# def isprime(n):
#     fc=0
#     for i in range(1,n+1):
#         if n%i==0:
#             fc=fc+1
#             if fc==2:
#                 return "prime"
#             else:
#                 return "not prime"
# def prime(a,b):
#     for i in range(a,b):
#         isprime(i)
#     print(i)
# a=8
# b=18
# prime(a,b)


#****palindrome using functions******
# def palin(n):
#     rev=0
#     k=n
#     while n>0:
#         r=n%10
#         rev=rev*10+r
#         n=n//10
#     if rev==k:
#         print("palindrome")
#     else:
#         print("not palindrome")
# n=2002
# print(palin(n))

#    OR
# def palin(n):
#     rev=0
#     k=n
#     while n>0:
#         r=n%10
#         rev=rev*10+r
#         n=n//10
#     return rev==k
# n=101
# j=palin(n)
# if j:
#     print("palin")
# else:
#     print("not palin")



#for range of numbers
# def palin(n):
#     rev=0
#     k=n
#     while n>0:
#         r=n%10
#         rev=rev*10+r
#         n=n//10
#     if rev==k:
#         return("palindrome")
#     else:
#         return ("not palindrome")
# def ispalin(a,b):
#     for i in range(a,b):
#         palin(i)
#     print(i)
# a=100
# b=203
# print(ispalin(a,b))







