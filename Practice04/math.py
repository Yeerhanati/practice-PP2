# Math and Random Module
import math
import random

# 1. Built-in math functions
nums = [3, 1, 4, 1, 5]
print("Min:", min(nums))
print("Max:", max(nums))
print("Absolute:", abs(-7))
print("Round:", round(3.1415, 2))
print("Power:", pow(2, 3))

# 2. Math module functions
print("Square root:", math.sqrt(16))
print("Ceil:", math.ceil(4.2))
print("Floor:", math.floor(4.8))
print("Pi:", math.pi)

# 3. Random module
print("Random float:", random.random())
print("Random int (1-10):", random.randint(1, 10))
print("Random choice:", random.choice(nums))

random.shuffle(nums)
print("Shuffled list:", nums)