# Single return value
def get_square(x):
    return x * x

# Multiple return values
def get_min_max(numbers):
    return min(numbers), max(numbers)

result = get_square(6)
print(result)

min_num, max_num = get_min_max([1, 2, 3, 4])
print(min_num, max_num)