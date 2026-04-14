# Write a program to convert a list of digits into a number.
# l =list(map(int,input().split()))
# num = 0
#
# for d in l:
#     num = num * 10 + d
#
# print(num)


#Write a program to convert a number into a list of digits.
# n = int(input())
# digits = []
# if n < 0:
#     n = -n
# while n > 0:
#     digit = n % 10
#     digits.insert(0, digit)
#     n = n // 10
#
# print(digits)




# Write a program to reverse a list and also reverse each element in the list.
# Example list (strings / digits as strings)
# lst = ["123", "45", "6789", "0"]
# reversed_elements = []
# for s in lst:
#     rev = ""
#     for char in s:
#         rev = char + rev
#     reversed_elements.append(rev)
#
#
# reversed_list = []
# for i in range(len(reversed_elements) - 1, -1, -1):
#     reversed_list.append(reversed_elements[i])
#
# print(reversed_list)





#Kth number
# num = int(input("Enter number: "))
# digits = [int(d) for d in str(num)]
#
# results = []
#
#
# first_sum = sum(digits)
# results.append(first_sum)
#
#
# for i in range(1, len(digits) + 1):
#     current_sum = sum(digits[i:])
#     total = current_sum + sum(results)
#     results.append(total)
#
#
# final_sum = sum(results[1:])
#
# if final_sum == num:
#     print("SUCCESS")
# else:
#     print("NOT SUCCESS")









#print frequency of the numbers  in asccending order
# l = [10, 20, 10, 20, 20, 17, 5, 17, 6]
# for i in range(len(l)):
#     c = l.count(l[i])
#     d=(f"{l[i]}->{c}")
#     print(d)