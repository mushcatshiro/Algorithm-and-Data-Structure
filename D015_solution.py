"""
Given a stream of elements too large to store in memory, pick a random element from the stream with uniform probability
"""

# basically hash table?

import random

def pick(big_stream):
    random_element = None

    for i, e in enumerate(big_stream):
        print(f'i: {i}; e: {e}')
        if i == 0:
            print(f'i==0, i: {i}')
            random_element = e
        elif random.randint(1, i + 1) == 1:
            print(f'randomint i: {i}')
            random_element = e
        print(f'random: {random_element}')
    return random_element


print(pick([1, 2, 3, 4, 5]))