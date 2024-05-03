#closures
#Decorators

def outer_function(x):
    def inner_function(y):
        return x + y

    return inner_function


outer = outer_function(147)
result = outer(17)

# print(result)


def create_counter():
    count = 0

    def increment():
        nonlocal count
        count += 1
        return count

    def reset():
        nonlocal count
        count = 0
        return count

    def get_count():
        return count

    return increment, reset, get_count()


increment_counter, reset_counter, get_counter = create_counter()
# print(increment_counter())
# print(increment_counter())
# print(increment_counter())
# print(increment_counter())
# print('------------------------')
# print(reset_counter)
# print('------------------------')

#Decorator


# def my_decorator(func):
#     def wrapper(*args, **kwargs):
#         print('Calling function before ')
#         print(func(*args, **kwargs))
#
#     return wrapper
#
#
# @my_decorator
# def say_hello():
#     print('Hello')
#
#
# say_hello()

import time


def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f'{func.__name__}: {end - start}s')
        return result, end - start

    return wrapper

@timer
def factorial(n):
    if n == 0:
        return 1

    return n * factorial(n - 1)


print(factorial(10))