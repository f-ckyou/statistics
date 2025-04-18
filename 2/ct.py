
from collections import Counter

# simple method
marks = [56, 34, 34, 56, 67, 76, 342]
n = len(marks)

# Mean
mean = sum(marks) / n
print(f"Mean = {mean}")

# Median
sorted_marks = sorted(marks)

if n % 2 == 0:
    mid1 = sorted_marks[n // 2 - 1]
    mid2 = sorted_marks[n // 2]
    median = (mid1 + mid2) / 2
else:
    median = sorted_marks[n // 2]

print(f"Median = {median}")


# mid_index = n // 2
# if n % 2 == 0:
#     median = (sorted_marks[mid_index - 1] + sorted_marks[mid_index]) / 2
# else:
#     median = sorted_marks[mid_index]
# print(f"Median = {median}")

# Mode
# 


marks_counts = Counter(marks)  # dictionary
# print(marks_counts) 
max_count = max(marks_counts.values())
# print(max_count)

modes = [marks for marks, count in marks_counts.items() if count == max_count]

if len(modes) == n:
    print("Mode: No unique mode")
elif len(modes) == 1:
    print(f"Mode: {modes[0]}")
else:
    print(f"Modes: {modes}")

