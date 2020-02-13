import functools
import os
import time


def computation_time( message="Compuation Time"):
    """ Testing the computation time of a function 
        Returns only one Value, may require unpacking
    """
    def wrapper_repeat(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            """Wrap the function with start and finish times"""

            start_time = time.time()

            value = func(*args, *kwargs)

            end_time = time.time()

            print(message)
            print("\t",end_time - start_time, "in seconds")


            return value

        return wrapper
    
    return wrapper_repeat
