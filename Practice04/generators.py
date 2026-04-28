# Iterators and Generators Practice

# 1. Basic Iterator with iter() and next()
my_list = [10, 20, 30]
my_iterator = iter(my_list)

print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))

# 2. Loop through an iterator
for num in my_list:
    print(num)

# 3. Custom Iterator class
class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 3:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration

my_class = MyNumbers()
my_iter = iter(my_class)

for x in my_iter:
    print(x)

# 4. Generator function with yield
def my_generator():
    yield 1
    yield 2
    yield 3

for value in my_generator():
    print(value)

# 5. Generator Expression
gen_exp = (x * 2 for x in range(1, 4))
for num in gen_exp:
    print(num)