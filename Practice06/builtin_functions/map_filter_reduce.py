# map(), filter(), reduce() functions
from functools import reduce

numbers = [1, 2, 3, 4, 5]

# map(): apply function to all items
squared = list(map(lambda x: x**2, numbers))
print("Squared numbers:", squared)

# filter(): select items by condition
even = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers:", even)

# reduce(): aggregate values
total = reduce(lambda a, b: a + b, numbers)
print("Sum of list:", total)