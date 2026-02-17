#hcf for 2 values
# a=int(input())
# b=int(input())
# if a<b:
#     l=a
# else:
#     l=b
# for i in range(l,0,-1):
#     if a%i==0 and b%i==0:
#         print(i)
#         break

#hcf fo 3 values
# a=int(input())
# b=int(input())
# c=int(input())
# if a<b and a<c:
#     l=a
# elif b<c:
#     l=b
# else:
#     l=c
# for i in range(l,0,-1):
#     if a%i==0 and b%i==0 and c%i==0:
#         print(i)
#         break


#lcm for 2 value
# a=int(input())
# b=int(input())
# if a>b:
#     h=a
# else:
#     h=b
#
# k=h
# while(True):
#     if h%a==0 and h%b==0:
#         print(h)
#         break
#     h=h+k

#Write a program to print the LCM of given two numbers
# n1=int(input())
# n2=int(input())
# if n1<=0 and n2<=0:
#     print("Invalid Inputs.")
# elif n1<=0:
#     print("Invalid First Input")
# elif n2<=0:
#     print("InValid Second Input")
# else:
#     h=max(n1,n2)
#     k=h
#     while(True):
#         if(h%n1==0 and h%n2==0):
#             print(h)
#             break
#         h=h+k


#Write a program to print the GCD of given three numbers?
# a=int(input())
# b=int(input())
# c=int(input())
# l=min(a,b,c)
# if (a<=0 and b<=0)or(b<=0 and c<=0)or(c<=0 and a<=0):
#     print("Invalid Inputs")
# elif a<=0:
#     print("Invalid First Input")
# elif b<=0:
#     print("Invalid Second Input")
# elif c<=0:
#     print("Invalid Third Input")
# else:
#     for i in range(l, 0, -1):
#         if (a%i ==0 and b%i==0 and c%i==0):
#             print(i)
#             break


#Write a program to print the LCM of given three numbers.
# n1 = int(input())
# n2 = int(input())
# n3 = int(input())
# c = 0
#
# if n1 <= 0:
#     c += 1
# if n2 <= 0:
#     c += 1
# if n3 <= 0:
#     c += 1
# if c >= 2:
#     print("Sorry Invalid Inputs!")
#
# elif n1 <= 0:
#     print("Invalid First Input")
# elif n2 <= 0:
#     print("Invalid Second Input")
# elif n3 <= 0:
#     print("InvaliD ThirD Input")
# else:
#     h = max(n1, n2, n3)
#     k = h
#     while (True):
#         if h % n1 == 0 and h % n2 == 0 and h % n3 == 0:
#             print(h)
#             break
#         h = h + k




#Write a program to print the GCD of given two numbers?
# a=int(input())
# b=int(input())
# l=min(a,b)
# if a<=0 and b<=0:
#     print("Invalid Inputs")
# elif a<=0:
#     print("Invalid First Input")
# elif b<=0:
#     print("Invalid Second Input.")
# else:
#     for i in range(l, 0, -1):
#         if a%i==0 and b%i==0:
#             print(i)
#             break

