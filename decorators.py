'''a decorator is a function that takes another function, 
extends the behavior of the latter function,
without explicitly modifying it'''

# we require functools just if we refer to function
# giving us it's original name instead of wrapper and decorator.
import functools
import time


def decorator(func):
    ''' Decorator boiler plate.'''
    @functools.wraps(func)
    def wrapper_decorator(*args, **kwargs):
        # Do something here.
        value = func(*args, **kwargs)
        # Do something here.
        return value
    return wrapper_decorator

def timer(func):
    ''' Prints the runtime of decorated function '''
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start = time.perf_counter()
        value = func(*args, **kwargs)
        end = time.perf_counter()
        run_time = end - start
        # Use dunder __name__ with !r flag to make sure it uses repr version of name.
        # Use :.4f to get in 4 places of decimal precision.
        print(f"Finished {func.__name__!r} in {run_time:.4f} secs")
        return value
    return wrapper_timer


