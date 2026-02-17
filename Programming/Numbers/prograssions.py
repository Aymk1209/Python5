#arthamatic
# s=int(input("enter starting number:"))
# d=int(input("enter differ of numbers:"))
# n=int(input("no.of teems:"))
# for i in range(n):
#     print(s+(i*d))

#sum of num in ap
# s=int(input("enter starting number:"))
# d=int(input("enter differ of numbers:"))
# n=int(input("no.of teems:"))
# sum=0
# for i in range(n):
#     k=s+(i*d)
#     sum=sum+k
# print(sum)

# #finding nth value in series AP
# s=int(input("enter starting number:"))
# d=int(input("enter differ of numbers:"))
# n=int(input("no.of teems:"))
# for i in range(n):
#     print(s+(n-1)d)



##Write a Program to Print first 'n' Numbers by taking input of
#  # term(a), common difference(d) and no of terms(n) in the Arithmetic progression series?
# a=int(input())
# d=int(input())
# n=int(input())
# if n<=0:
#     print("Invalid Input.")
# else:
#     c=0
#     for i in range(n):
#         k=a+(i*d)
#         c=c+1
#         if c>1:
#             print(end=", ")
#         print(k,end="")
#     print('.')



##Write a Program to Print first 'n' Numbers by taking input of 1st term(a)
#common difference(d) and no of terms(n) in the Harmonic progression series?
# a=int(input())
# d=int(input())
# n=int(input())
# if n<=0:
#     print("Invalid Input")
# else:
#     c=0
#     for i in range(n):
#         k=1/(a+(i*d))
#         c=c+1
#         if c>1:
#             print(end=", ")
#         print("%.2f"%k,end="")



#Write a Program to Print first 'n' Numbers by taking input of 1st term(a)
#common Ratio(r) and No of terms(n) in the geometric progression series ?
# a=int(input())
# r=int(input())
# n=int(input())
# if n<=0:
#     print("Invalid Input.")
# else:
#     c=0
#     for i in range(n):
#         k=a*r**i
#         c=c+1
#         if c>1:
#             print(end=", ")
#         print(k,end="")
#     print(".")


#Write a Program to Print sum of the first 'n' terms by taking input of
#1st term(a), common ratio(r) and No of terms(n) in the Geometric progression series?
# a=int(input())
# r=int(input())
# n=int(input())
# sum=0
# if n<=0:
#     print("Invalid Input")
# else:
#     for i in range(n):
#         k=a*r**i
#         sum=sum+k
#     print(sum)


#Write a Program to Print sum of the first 'n' terms by taking input of 1st term(a)
#common difference(d) and No of terms(n) in the Arithmetic progression series?
# a=int(input())
# d=int(input())
# n=int(input())
# if n<=0:
#     print("Invalid input.")
# else:
#     sum=0
#     for i in range(n):
#         k=a+i*d
#         sum=sum+k
#         if i==n-1:
#             print(k,end=" = ")
#         else:
#             print(k,end=" + ")
#     print(sum,end=".")



#Write a Program to Print sum of the first 'n' terms by taking input of 1st term(a)
#common difference(d) and No of terms(n) in the Harmonic progression series?
# a=int(input())
# d=int(input())
# n=int(input())
# sum=0
# if n<=0:
#     print("Invalid Input.")
# else:
#     for i in range(n):
#         k=1/(a+(i*d))
#         sum=sum+k
#     print("%0.2f"%sum)


#Find and Print the
 # term value in the Arithmetic progression series by taking input of 1st term(a), common difference(d) and
 # term ?
# a=int(input())
# d=int(input())
# n=int(input())
# if n<=0:
#     print("InValid Input.")
# else:
#     print(f"Last term value is : {a+d*(n-1)}.")


#Find the nth term value in the Harmonic progression series by taking input of 1st term(a),
# common difference(d) and nth term ?
# a=int(input())
# b=int(input())
# n=int(input())
# if n>0:
#     print(f"{round(1/(a+b*(n-1)),2):.2f}")
# else:
#     print("InvaliD InPut")


#Find the nth term value in the geometric progression series by taking input of 1st term(a),
# common Ratio(r) and nth term ?
# a=int(input())
# r=int(input())
# n=int(input())
# if n>0:
#     print(f"Last term value is : {a * r ** (n-1)}.")
# else:
#     print("InValid Input.")






