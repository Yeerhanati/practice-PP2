# Move and copy files between directories
import shutil
import os

# Create test folder
os.mkdir("test_folder")

# Copy file to new folder
shutil.copy("sample.txt", "test_folder/sample.txt")
print("File copied to folder.")

# Move file
shutil.move("test_folder/sample.txt", ".")
print("File moved back.")

# Clean up
os.rmdir("test_folder")
print("Test folder removed.")