# if __name__ == '__main__':
#     x = int(input())

# n=1
# while (n<=n):
#
#     n=n+1
#     print(n, end=" ")

# x=1
# while (x <= 10):
#     print(x, end="\t\n")
#     x += 1

def hello_func(greeting, name='You'):
    return '{}, {}.'.format(greeting, name)

print(hello_func('Hi', name='Prashant'))


def student_info(*args, **kwargs):
    print(args)
    print(kwargs)
    
# student_info('Math','English', name='john', age=28, contact='+91-9650652930')
courses = ['Math','English']
info = {'name': 'john', 'age': 28, 'contact': '+91-9650652930'}

student_info(*courses, **info)      # To unpack the dictionary * & ** is being used
