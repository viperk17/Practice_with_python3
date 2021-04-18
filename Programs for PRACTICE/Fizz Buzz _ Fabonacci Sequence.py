# from pip._vendor.urllib3.connectionpool import xrange
# import itertools

# # for num in xrange(1,101):
# #     if num%5==0 and num%3==0:
# #         print("Fizz Buzz")
# #     elif num % 5 == 0:
# #         print("Buzz")
# #     elif num % 3 == 0:
# #         print("Fizz")
# #     else:
# #         print(num)


# # #Fibonacci Sequence
# # a, b = 0, 1
# # for i in xrange(0,10):
# #     print(a)
# #     a, b = b, a +b


# # Fibonacci Generator
# '''xrange return the one no at a time while range return all the 
# items in the memory'''


# def fib(num):
#     a, b = 0, 1
#     for i in xrange(0, num):
#         yield "{}: {}".format(i + 1, a)
#         a, b = b, a + b


# for item in fib(10):
#     print(item)

# # Dict iteration
# '''iteritems() returns one item at a time
# while items() return all the items in the memory'''
# my_dict = {'name': 'Prashant', 'age': '25', 'job': 'Developer'}
# for key, val in my_dict.iteritems():
#     print("My {} is {}".format(key, val))

# # #List comprehensions
# # my_list = [1,2,3,4,5,6,,7,8,9,10]
# #
# # #Gives the square of no in list
# # squares = [num*num for num in my_list]
# # print(squares)

# d = {1:[1,2,3],2:(4,6,8)}
# d[1].append(4)
# print(d[1],end="")
# L=list(d[2])
# L.append(10)
# d[2]=tuple(L)
# print(d[2])

# value= [1,2,3,4]
# data =0
# try:
#     data =value[3]
# except IndexError:
#     print('HR IndexError',end="")
# except:
#     print('HackerRank IndexError',end="")
# finally:
#     print('Finally IndexError',end="")

# data =10
# try:
#     data = data/0
# except ZeroDivisionError:
#     print('HR ZeroDivisionError',end="")
# finally:
#     print("Finally ZeroDivisionError",end="")


# b=[0,1,2,3,4,5,6,7,8,9]
# print(b[::3])


# D = {1:1,2:'2','1':1,'2':3}
# D['1']=2
# print(D[D[D[str(D[1])]]])

# T = (1,2,3,4,5,6,7,8)
# # print(T[T.index(5)], end=" ")
# # print(T[T[T[6]-3]-6])
# print(T[T.index(5)])