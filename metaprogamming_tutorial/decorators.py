# Decorators

# def debug(func):
#     # func is a function to be wrapped
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         # print(func.__name__)
#         print(func.__qualname__)
#         return func(*args, **kwargs)
#     return wrapper


# def outer_function(msg):
#     def inner_function():
#         print(msg)
#     return inner_function

# hi_func = outer_function('Hello')
# bye_func = outer_function('bye')
#
# hi_func()
# bye_func()


def decorator_function(original_function):
    def wrapper_function():
        print('wrapper executed this before "{}" function'.format(original_function.__name__))
        original_function()
    return wrapper_function

def display():
    print('display funciton ran')

@decorator_function
def test_display():
    print('some other function ran')

decorated_display = decorator_function(display)
decorated_display()
test_display()
