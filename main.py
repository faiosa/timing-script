"""
This script is used to compare spent time for 'for' loop, list comprehension, map function, generator expression and generator function

Additional modules:
    - mytimer: used to record spend time
"""

import sys
import mytimer

# Print Python version
print(sys.version)

reps = 10000
repsList = range(reps)


def forLoop():
    res = []
    for x in repsList:
        res.append(abs(x))
    return res


def listComprehension():
    return [abs(x) for x in repsList]


def mapFunction():
    return map(abs, repsList)


def generatorExpression():
    return list(abs(x) for x in repsList)


def generatorFunction():
    def generator():
        for x in repsList:
            yield abs(x)
        return list(generator())


# Calculate time spent by each of the sequences
for x in (forLoop, listComprehension, mapFunction, generatorExpression, generatorFunction):
    elapsed_time = mytimer.timer(x)
    print("-" * 31)
    print(f"{x.__name__} take {elapsed_time} to complete!")
