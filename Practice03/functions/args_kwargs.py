# *args - variable positional arguments
def sum_all(*args):
    return sum(args)

# **kwargs - variable keyword arguments
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print(sum_all(1, 2, 3, 4))
print_info(name="Tom", age=20, grade="A")