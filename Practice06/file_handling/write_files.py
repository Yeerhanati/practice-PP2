# Write and append files using with statement

# Write (overwrite)
with open("sample.txt", "w", encoding="utf-8") as f:
    f.write("Hello, File Handling!\n")
    f.write("Python is powerful.\n")

# Append new content
with open("sample.txt", "a", encoding="utf-8") as f:
    f.write("This line is appended.\n")

print("File write and append completed.")