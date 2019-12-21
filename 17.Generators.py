#how to use generators
def square_numbers(nums):
    for i in nums:
        yield i * i

# my_nums = square_numbers([1,2,3,4,5])
my_nums = [x*x for x in [1,2,3,4,5]]
# my_nums = (x*x for x in [1,2,3,4,5])

# print(my_nums)
print(list(my_nums))

# for num in my_nums: #my_nums is the generator
#     print(num)

#Prints the elements one by one
# print(next(my_nums))
# print(next(my_nums))
# print(next(my_nums))
# print(next(my_nums))
# print(next(my_nums))
