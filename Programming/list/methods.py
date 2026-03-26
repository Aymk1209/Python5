# Write a program to create a list by taking input from the user and print the list.
# l=list(map(int,input().split()))
# print(l)
#if user first gives number of elements present in the list and gives values
# l=[]
# n=int(input("size of list:"))
# for i in range(n):
#     print("enter the numbers in one line by line")
#     k=int(input())
#     l.append(k)
# print(l)



#2
# Write a program to insert an element at a specific index in a list.
# l=[10,20,40,50]
# l.insert(2,30)
# print(l)
# print(*l)


#3
#Write a program to merge two lists into a single list.
# l=[10,20,30,40]
# l2=[50,60,70,80]
# l.extend(l2)
# print(l)

     #or
# l3=l+l2
# print(*l3)


#4
#Write a program to remove a specific element from a list.
# l=[10,20,30,40,50]
# a=int(input("enter removing number:"))
# if a in l:
#     l.remove(a)
#     print(l)
# else:
#     print("not found")


#5
# #Write a program to remove an element from a list using its index.
# l=[10,20,30,40,50]
# a=int(input("enter removing number:"))
#     if(a>=-(len(l) and a<(len(l))):
#         l.pop(a)
#         print(*l)
#     else:
#         print("Invalid")



#6
#Write a program to find the index of a given element in a list.
# l=[10,20,30,40,50]
# a=int(input("enter removing number:"))
# if a in l:
#     k=l.index(a)
#     print(k)
# else:
#     print("not found")




#7
# Write a program to count the number of occurrences of an element in a list.
# l=[10,20,10,30,40,10,50,60,10,70]
# k=l.count(10)
# print(k)
# j=l.count(100)
# print(j)




#8
#Write a program to find the sum of the first and last elements of a list.
# l=[10,20,30,40,50]
# a=l[0]
# b=l[-1]
# l=a+b
# print(l)



#9
#Write a program to calculate the sum of list elements up to a given index.
# l=[10,20,30,40,50]
# index=int(input("enter index value"))
# total=0
# for i in range(index+1):
#     total+=l[i]
# print(total)



#10
# Write a program to calculate the average of odd numbers in a list.
# l = [10, 15, 20, 25, 30, 35, 40]
# total = 0
# count = 0
#
# for num in l:
#     if num % 2 != 0:  # Check if odd
#         total += num
#         count += 1
#
# if count > 0:
#     average = total / count
#     print(f"Average of odd numbers: {average:.2f}")
# else:
#     print("No odd numbers")



#11
# Write a program to print all prime numbers present in a list.
# l=list(map(int,input().split()))
# for i in range(len(l)):
#     fc=0
#     for j in range(1,l[i]+1):
#         if(l[i]%j==0):
#             fc=fc+1
#     if fc==2:
#         print(l[i],end=" ")


#12
# Write a program to print the next prime number for each element in the list





#13
#Write a program to print the list in reverse order.
# l=[1,2,3,4,5,6,7]
# l.reverse()
# print(l)

#14
#Write a program to find sum of any two elements which is equal to key value
# l=list(map(int,input().split()))
# k=int(input())
# for i in range(len(l)):
#     for j in(i+1,len(l)):
#         if(l[i]+l[j]==k):
#
#             print(f"{l[i]},{l[j]}")











#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#max and min
#15
# Write a program to find the largest number in a list.
# l=[1,2,3,7,5,6]
# h=0
# for num in l:
#     if num>h:
#         h=num
# print(h)
        #or
# l=list(map(int,input().split()))
# h=l[0]
# for i in range(len(l)):
#     if (l[i]>h):
#         h=l[i]
# print(h)


#16
#Write a program to find the second largest number in a list
# l=[1,2,3,4,5,6,7]
# l.sort(reverse=False)
# print(l[-2])
                 #or
# l=list(map(int,input().split()))
# h1=l[0]
# h2=h1
# for i in range(len(l)):
#     if l[i]>h1:
#         h2=h1
#         h1=l[i]
#     elif l[i]>h2:
#         h2=l[i]
# print(h2)


#17
# #. Write a program to find the third largest number in a list.
# l=[1,2,3,4,5,6,7]
# l.sort(reverse=False)
# print(l[-3])
                   #or
# l=list(map(int,input().split()))
# h1=l[0]
# h2=h1
# h3=h2
# for i in range(len(l)):
#     if l[i]>h1:
#         h3=h2
#         h2=h1
#         h1=l[i]
#     elif l[i]>h2:
#         h3=h2
#         h2=l[i]
#     elif l[i]>h3:
#         h3=l[i]
# print(h3)



#18
# # Write a program to sort a list without using any built-in sorting functions.
# l=[7,6,5,4,3,2,1]
# j=
# for num in l:
#     if num>j:
#         j=num
#     print(j)

           #or
# l = list(map(int, input().split()))
# for i in range(len(l)):
#     for j in range(i+1,len(l)):
#         if l[i]>l[j]:
#             l[i],l[j]=l[j],l[i]
# print(l)




#19
# to find nth largest number in list without in bulit
# l = list(map(int, input().split()))
# n=int(input())
# for i in range(len(l)):
#     for j in range(i+1,len(l)):
#         if l[i]>l[j]:
#             l[i],l[j]=l[j],l[i]
# print(l[len(l)-n])



#to find first four smallest missing values in list
# l = list(map(int, input().split()))
# s=min(l)+1
# c=0
# while(c<4):
#     if s not in l:
#         print(s)
#         c+=1
#     s=s+1




