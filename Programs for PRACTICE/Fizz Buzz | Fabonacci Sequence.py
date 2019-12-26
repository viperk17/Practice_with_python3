from pip._vendor.urllib3.connectionpool import xrange
import itertools

# for num in xrange(1,101):
#     if num%5==0 and num%3==0:
#         print("Fizz Buzz")
#     elif num % 5 == 0:
#         print("Buzz")
#     elif num % 3 == 0:
#         print("Fizz")
#     else:
#         print(num)


# #Fibonacci Sequence
# a, b = 0, 1
# for i in xrange(0,10):
#     print(a)
#     a, b = b, a +b


#Fibonacci Generator
'''xrange return the one no at a time while range return all the 
items in the memory'''
def fib(num):
    a, b = 0, 1
    for i in xrange(0, num):
        yield "{}: {}".format(i+1, a)
        a, b = b, a+b

for item in fib(10):
    print(item)

#Dict iteration
'''iteritems() returns one item at a time
while items() return all the items in the memory'''
my_dict = {'name':'Prashant', 'age':'25', 'job':'Developer'}
for key, val in my_dict.iteritems():
    print("My {} is {}".format(key, val))


# #List comprehensions
# my_list = [1,2,3,4,5,6,,7,8,9,10]
#
# #Gives the square of no in list
# squares = [num*num for num in my_list]
# print(squares)