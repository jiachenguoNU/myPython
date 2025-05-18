def square(x):
    return x * x

def print_running(f, x): # pass a function as an argument
    print(f'"{f.__name__}" is running.')
    return f(x)

result = print_running(square, 2)


def decorator(func):
    def wrapper(*args,**kwargs):
        print(f'{func.__name__} is running')
        result = func(*args,**kwargs)    
        return result
    return wrapper



# decorator to record the time taken by a function
import time


# define a decorator function
def timeit_fun(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f'{func.__name__} took {end - start:.4f} seconds')
        return result
    return wrapper


decorated_square = timeit_fun(square)
result = decorated_square(10)

# python decorator syntax
@timeit_fun
def square(x):
    return x * x

result = square(10)


# decorator with additional arguments
def repeat(num_times):
    def decorator_repeat(func):
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator_repeat #addtional return statement for the argumented decorator

@repeat(num_times=3)
def greet(name):
    print(f'Hello, {name}!')

greet('Alice')
print(greet.__name__) #wrapper is the name of the function

import functools

def repeat(num_times):
    
    def decorator_repeat(func):
        @functools.wraps(func) ############ this decorator is used to preserve the metadata of the original function
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator_repeat #addtional return statement for the argumented decorator

@repeat(num_times=3)
def greet(name):
    print(f'Hello, {name}!')

greet('Alice')
print(greet.__name__) #wrapper is the name of the function
