def squares_up_to(n):
    for i in range(n + 1):
        yield i ** 2

n = int(input("Enter a number: "))
for square in squares_up_to(n):
    print(square)