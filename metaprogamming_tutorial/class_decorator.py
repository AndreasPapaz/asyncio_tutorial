# Class Decorators

def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):
        print('wrapper executed this before "{}" function'.format(original_function.__name__))
        return original_function(*args, **kwargs)
    return wrapper_function


class decorator_class(object):
    def __init__(self, original_function):
        self.original_function = original_function

    def __call__(self, *args, **kwargs):
        print('call method executed this before "{}" function'.format(self.original_function.__name__))
        return original_function(*args, **kwargs)


@decorator_class
def display_info(name, age):
    print('display_infor from class ran with args ({}, {})'.format(name, age))
