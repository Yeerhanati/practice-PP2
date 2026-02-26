def squares_up_to(n):
    for i in range(n + 1):
        yield i ** 2

# Example usage:
for square in squares_up_to(10):
    print(square)