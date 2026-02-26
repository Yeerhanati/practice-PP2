from datetime import datetime

# 示例：计算两个具体日期时间的差（秒）
date1 = datetime(2024, 2, 26, 12, 0, 0)
date2 = datetime(2024, 2, 26, 12, 5, 30)

difference = date2 - date1
seconds = difference.total_seconds()
print(f"Difference in seconds: {seconds}")