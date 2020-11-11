
"""
This module is used to run a function with optional attributes 1000 times.
"""

import time


def timer(func, *args, **kwargs):
    start = time.clock()

    for rep in range(1000):
        func(*args, **kwargs)

    finish = time.clock()

    elapsed_time = finish - start
    return elapsed_time
