import re

emails = [
    "correct.email@example.com",
    "incorrect-email-at-example.com",
    "another.correct.email@example.org"
]

pattern = r"[\w.-]+@[\w-]+\.[a-z]{2,3}"

for email in emails:
    if re.search(pattern, email):
        print(f"{email} is valid")
    else:
        print(f"{email} is invalid")
