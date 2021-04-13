def prefix_decorator(prefix):
    def decorator_function(origional_function):
        def wrapper_function(*args, **kwargs):
            print(prefix, 'Execution Before', origional_function.__name__)
            result = origional_function(*args, **kwargs)
            print(prefix, 'Executed After', origional_function.__name__, '\n')
            return result

        return wrapper_function

    return decorator_function


@prefix_decorator('Testing : ')  # adds prefix before the print stats in wrapper func
def display_info(name, age):
    prefix_decorator('display_info ran with arguments ({}, {})'.format(name, age))


display_info('Jonas', 22)
display_info('Rohini', 29)
