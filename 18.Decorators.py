# Decorators : Dynamically Alter the functionality of the function
'''
first class functions allow us to treat functions like any other objects
We can pass functions as arguments to other functions. Closure allows us to take advantage of first class function and return inner function that remember and has access var local to the scope in which they were created
'''

# def outer_function():
#     message = 'Hi'
from orca.sound import args

'''
def outer_function(msg):
    message = msg
    def inner_function():  # inner function has access to var message
        print(msg)

    return inner_function()


hi_func = outer_function('Hi')
bye_func = outer_function('Bye')

hi_func
bye_func
'''

'''
Decorator is a function that takes another function as an argument, adds some functionality
and returns another functions without altering the source code
'''


def decorator_function(origional_function):
    def wrapper_function(*args, **kwargs):  # inner function has access to var message
        print('wrapper executed this before {}'.format(origional_function.__name__))
        return origional_function(*args, **kwargs)

    return wrapper_function


# #Using class
# class decorator_class(object):
#     def __init__(self, origional_function):
#         self.origional_function = origional_function
#
#     def __call__(self, *args, **kwargs):
#         print('call method executed this before {}'.format(self.origional_function.__name__))
#         return self.origional_function(*args, **kwargs)

@decorator_function  # for class use - @decorator_class
def display():
    print('Display function ran...')


# decorated_display = decorator_function(display)
# decorated_display()
@decorator_function
def display_info(name, age):
    print('display_info ran with arguments ({}, {})'.format(name, age))


display_info('Josh', 28)

display()
