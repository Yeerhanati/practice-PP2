# Copy and delete files
import shutil
import os

# Copy file
shutil.copy("sample.txt", "sample_backup.txt")
print("File copied successfully.")

# Delete file safely
if os.path.exists("sample_backup.txt"):
    os.remove("sample_backup.txt")
    print("Backup file deleted.")
else:
    print("File does not exist.")