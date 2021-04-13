# map function converts a string,etc into a list
# numbers = ["3","4","5","25"]
#
# print(map(int, numbers))
# numbers = list(map(int, numbers))


# for i in range(len(numbers)):
#     numbers[i] = int(numbers[i])
#
#
# numbers[2] = numbers[2] + 1
# print(numbers[2])

# num = [2,3,4,7,5,2,4,6,5]
#
# def sq(a):
#     return a*a
#
# square = list(map(sq, num))
# print(square)


################################## Using Lambda ###########
# def square(a):
#     return a*a
#
# def cube(a):
#     return a*a*a
#
# func = [square, cube]
# num = [2,3,4,7,5,2,4,6,5]
# for i in range(5):
#     val = list(map(lambda x:x(i), func))
#     print(val)

######################### Filter ###################################
# list1 = [1,2,3,4,5,6,7,8,9]
#
# def is_greater_5(num):
#     return num > 5
#
# gr_than_5 = list(filter(is_greater_5, list1))
# print(gr_than_5)


###################### REDUCE #######################
# part of func tools
from functools import reduce

list2 = [1, 2, 3, 4]
print(num)
num = reduce(lambda x, y: x + y, list2)
print(num)

# num = 0
# for i in list2:
#     num = num+i
# printpr(num)
