'''uniformly pick a random element from a giant stream of data.
naively process the stream of data identifying each one we encounter in a list, find the size and pick a random element. would take O(N). better solution: solve using loop invariants=a statement about an algorithm's loop that: is true before the first iteration of the loop and. if it's true before an iteration, then it remains true before the next iteration
'''

import random


def pick(big_stream):
    random_element = None

    for i, e in enumerate(big_stream):
        #base case
        if i == 0:
            random_element = e
        if random.randint(1, i + 1) == 1:
            random_element = e
    return random_element

#since we are storing a single variable, this only takes up constant space 0(1)