def add(x, y):
    """Add Function"""
    return x + y


def subtract(x, y):
    """Subtract Function"""
    return x - y


def multiply(x, y):
    """Multiply Function"""
    return x * y


def divide(x, y):
    """Divide Function"""
    # return x / y
    if y == 0:
        raise ValueError('Cannot divide by zero')
    return x / y

# print(add(15,25))
