# enumerate(), zip(), sorted(), basic functions

# enumerate(): index + value
fruits = ["apple", "banana", "orange"]
for idx, fruit in enumerate(fruits):
    print(f"Index {idx}: {fruit}")

# zip(): pair two lists
names = ["Alice", "Bob"]
ages = [20, 22]
combined = list(zip(names, ages))
print("\nZipped lists:", combined)

# sorted()
nums = [5, 2, 9, 1]
print("Sorted:", sorted(nums))

# Basic built-ins
print("Length:", len(nums))
print("Sum:", sum(nums))
print("Min:", min(nums))
print("Max:", max(nums))