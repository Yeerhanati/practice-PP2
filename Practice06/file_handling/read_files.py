# File reading examples: read(), readline(), readlines()

# Read entire file
with open("sample.txt", "r", encoding="utf-8") as f:
    content = f.read()
print("Full content:\n", content)

# Read line by line
with open("sample.txt", "r", encoding="utf-8") as f:
    line1 = f.readline()
    line2 = f.readline()
print("\nLine 1:", line1.strip())
print("Line 2:", line2.strip())

# Read all lines into a list
with open("sample.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
print("\nAll lines list:", lines)