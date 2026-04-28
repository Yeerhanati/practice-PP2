# Date and Time Operations
from datetime import datetime, timedelta

# 1. Current date and time
now = datetime.now()
print("Current datetime:", now)
print("Year:", now.year)
print("Month:", now.month)

# 2. Create date object
my_birthday = datetime(2000, 5, 15)
print("Birthday:", my_birthday)

# 3. Date formatting
formatted = now.strftime("%Y-%m-%d %H:%M:%S")
print("Formatted date:", formatted)

# 4. Calculate time difference
future = now + timedelta(days=7)
print("Date after 7 days:", future)

diff = future - now
print("Difference in days:", diff.days)