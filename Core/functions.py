# a=int(input())
# def x():
#     a=10
# print(a)


# a=6
# def fname():
#     global a
#     a=10
#     print(a)
# print((a))
# fname()
# print(a)


# def fun(a):
#     print(a)
# fun(1)
# fun(2)


# def fun(a,b,c):
#     print(a+b+c)
# fun(1,2,3)
# fun(10,20)

# def fun(a=10):
#     print(a)
# fun(50)
# fun()

# def fun(c,b,a=10):
#     print(a+b+c)
# fun(20,50)
# fun(20,50,30)

# def fun(a,b):
#     y=a*b
#     return y
# fun(1,10)
# print(fun(10,3))
# a=fun(10,30)
# print(a)
# print(a+5)

# def fun(a,b=10):
#     print(a+b)
#     return(a*b)
# print(fun(5))

#to find BIGGEST of 3 parameters
# def fun(a,b=0,c=0):
#     if(a>b and a>c):
#         print ("a is big")
#     elif b>c:
#         print("b is big")
#     else:
#         print('c is big')
# fun(3)


#create a fun which cheeks "marks" of  a person pass fail
# def fun(marks):
#     if marks>40:
#         print("pass")
#     else:
#         print("Fail")
# fun(80)

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

#lambda functions:
# def fun(x):
#     x(50,70)
# fun(lambda x,y:print(x+y))

#map:
l=[1,2,3,4]
print(list(map(lambda x:x*2,l)))

