#the each element in list should print and how many times it is present in list
l=[10,20,10,20,20,17,5,17,6]
for i in range(len(l)):
    c=l.count(l[i])
    print(f"{l[i]}->{c}")

                #or

# l=[10,20,10,20,20,17,5,17,6]
# for i in range(len(l)):
#     c=0
#     for j in range(len(l)):
#         if(l[i]==l[j]):
#             c=c+1
#     print(f"{l[i]}->{c}")


#to find unique elements in list
# l=[10,20,10,20,20,17,5,17,6]
# for i in range(len(l)):
#     c=0
#     for j in range(len(l)):     #or c=l.count(l[i])
#         if(l[i]==l[j]):
#             c=c+1
#     if c==1:
#         print(l[i])


# #to find highest unique value
# l=[10,20,10,20,20,17,5,17,6]
# h=float("-inf")
# for i in range(len(l)):
#     c=0
#     for j in range(len(l)):     #or c=l.count(l[i])
#         if(l[i]==l[j]):
#             c=c+1
#     if c==1:
#         if l[i]>h:
#             h=l[i]
# print(h)



#to find lowest unique value
# l=[10,20,10,20,20,17,5,17,6]
# l1=float("inf")
# for i in range(len(l)):
#     c=0
#     for j in range(len(l)):     #or c=l.count(l[i])
#         if(l[i]==l[j]):
#             c=c+1
#     if c==1:
#         if l[i]<l1:
#             l1=l[i]
# print(l1)



#to remove the repated  elements and print remainging elements in list
# l=[10,20,10,20,20,17,5,17,6,4]
# for i in range(len(l)):
#     c=0
#     for j in range(i):
#         if(l[i]==l[j]):
#             c=c+1
#     if c==0:
#         print(l[i])

            #or

# l=[10,20,10,20,20,17,5,17,6,4]
# for i in range(len(l)):
#     l1=l[0:i]
#     c=l1.count(l[i])
#     if c==0:
#         print(l[i])


#to remove the repated  elements and print remainging elements in
# list and how many times each element is there

# l=[10,20,10,20,20,17,5,17,6,4]
# for i in range(len(l)):
#     l1=l[0:i]
#     c=l1.count(l[i])
#     if c==0:
#         c1=l.count(l[i])
#         print(f"{l[i]}->{c1}")

#to print  only duplicate elements and how many times
# l=[10,20,10,20,20,17,5,17,6,4]
# for i in range(len(l)):
#     l1=l[0:i]
#     c=l1.count(l[i])
#     if c==0:
#         c1=l.count(l[i])
#         if c1>1:
#             print(f"{l[i]}->{c1}")


# given a list and gives a value which indicates that
# many times repeted elements should be print
# l=[10,20,10,20,20,17,5,17,6,4]
# k=int(input())
# for i in range(len(l)):
#     l1=l[0:i]
#     c=l1.count(l[i])
#     if c==0:
#         c1=l.count(l[i])
#         if c1==k:
#             print(f"{l[i]}->{c1}")



# #. Write a program to calculate the backward frequency of elements in a list.
# l=[10,20,10,20,20,17,5,17,6,4]
# for i in range(len(l)):
#     l1=l[0:i]
#     c=l1.count(l[i])
#     print(f"{l[i]}->{c}")



#***TYPES OF FREQUENCY***

# l=[10,7,10,20,8,20,20,5,17,7]
#total frequency=2,2,2,3,1,3,3,1,1,2  >>UNQ ELE 8,5,7
#include right frequency "7"=2,2,1,3,1,2,1,1,1,1  >> LIST ELE(!O) 10,8,20,5,17,7
#right frequency "7"=1,1,0,2,0,1,0,0,0,0  >> LE(0) 10,7,20,8,5,17
#include left frequency=1,1,2,1,1,2,3,1,1,2 >> DE(!O)10,7,20,8,5,17
# left frequency=0,0,1,0,0,1,2,0,0,1 DE(!0)10,20,7