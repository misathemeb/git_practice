
# making use of iter, next and itertools library
import itertools

# defining variables
max_money = 15
options = []

# array of object and tuple
cat_toys = [("laser", 1.99), ("scratcher", 10.99), ("fountain", 5.99), ("catnip", 15.99), ('dancer', 2.00)]

# calling the object with iter
cat_toy_iterator = iter(cat_toys)

# using the next() method to go through iterables
print(next(cat_toy_iterator))
print(next(cat_toy_iterator))
print(next(cat_toy_iterator))
print(next(cat_toy_iterator))

# making use of a tool from the imports to list a 2 toy spread
toy_combos = itertools.combinations(cat_toys, 2)

# for loop to iterate through possible toy combos with the condition not to exceed $15
for combo in toy_combos:
    toy1 = combo[0]
    cost_of_toy1 = toy1[1]
    toy2 = combo[1]
    cost_of_toy2 = toy2[1]
    if cost_of_toy1 + cost_of_toy2 <= max_money:
      options.append(combo)
      
# print the array try new combos ****
print(options) 