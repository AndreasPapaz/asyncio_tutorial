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


# def decorator_function(original_function):
#     def wrapper_function(*args, **kwargs):
#         print('wrapper executed this before "{}" function'.format(original_function.__name__))
#         return original_function(*args, **kwargs)
#     return wrapper_function
#
# def display():
#     print('display funciton ran')
#
# @decorator_function
# def test_display():
#     print('some other function ran')

# decorated_display = decorator_function(display)
# decorated_display()
# test_display()



# def display_info(name, age):
#     print('display_info ran with arguments ({}, {})'.format(name, age))


# display_info("Andreas", 27)


def my_logger(orig_func):
    import logging
    logging.basicConfig(filename='{}.log'.format(orig_func.__name__), level=logging.INFO)

    def wrapper(*args, **kwargs):
        logging.info(
            'Ran with Args: {}, and Kwargs: {}'.format(args, kwargs))
        return orig_func(*args, **kwargs)

    return wrapper

@my_logger
def display_info(name, age):
    print('display_info ran with arguments ({}, {})'.format(name, age))


display_info('Andrwas', 27)
