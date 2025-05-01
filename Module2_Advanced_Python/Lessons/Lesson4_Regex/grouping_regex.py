import re

# Grouping example: Split and capture parts of phone number
text = "123-456"
pattern = r"(\d+)-(\d+)"
match = re.search(pattern, text)

if match:
    print("Group 1:", match.group(1))  # 123
    print("Group 2:", match.group(2))  # 456
