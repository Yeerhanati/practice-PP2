# Directory creation and listing
import os

# Get current directory
print("Current directory:", os.getcwd())

# Create nested directories
os.makedirs("docs/reports", exist_ok=True)
print("Nested directory created.")

# List files and folders
items = os.listdir(".")
print("\nItems in current dir:", items)

# Remove empty directory
os.rmdir("docs/reports")
os.rmdir("docs")
print("Empty directories removed.")