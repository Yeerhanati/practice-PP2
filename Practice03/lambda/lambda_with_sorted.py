# Use lambda for custom sorting
students = [("Tom", 20), ("Jerry", 18), ("Anna", 22)]
sorted_students = sorted(students, key=lambda x: x[1])
print(sorted_students)