# pass the func as an argument and edit it's behavior and return it with the samename:
# we are calling the inner functins in the decorator
# create a variable ref with the same name of the wrapped func and make it make it refer to the return value of the inner function


# This formula is a good boilerplate template for building more complex decorators.

import functools


def decorator(func):
    @functools.wraps(func)  # to keep the original identity of the wraped functoin
    def wrapper_decorator(*args, **kwargs):
        # Do something before
        value = func(*args, **kwargs)
        # Do something after
        return value  # to keep the return value of the wrapped func

    return wrapper_decorator
