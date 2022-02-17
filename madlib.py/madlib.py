# # this is a game to practice putting strings together aka concatenation

# # variables


# adj = input("Adjective: ")
# verb = input("Verb: ")
# noun = input("Noun: ")

# madlib = f"Programming is so {adj}! \ It is not something that can be {verb}. \ I'm pretty sure {noun} likes to do it."
# print(madlib)

# guess the number (computer)

import random

def num_generator(maxnum):
    generator = random.randint(1, maxnum)
    return generator

print(num_generator(500))
