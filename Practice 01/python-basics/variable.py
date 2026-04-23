x = 5
y = "John"
print(x)
print(y)

x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0
print(x)
print(y)
print(z)

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)
