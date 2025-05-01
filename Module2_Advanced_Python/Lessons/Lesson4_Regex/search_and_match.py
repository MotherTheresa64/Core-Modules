import re

# Example: Validating email format
email = "kareem33-34-28@gmail.com"
found = re.search(r"[\w.-]+@[\w-]+\.[a-z]{2,3}", email)
if found:
    print(f"{found.group()} is a valid email!")

# Finding multiple emails
text = "You can contact me at t.p@gmail.com or travis-p2@codingtemple.com, traviscpeck@email.com"
emails = re.findall(r"[\w.-]+@[\w-]+\.[a-z]{2,3}", text)
print("All emails found:", emails)

# Matching HTTPS URLs from the start
url = "https://something.com"
secure = re.match(r"https", url)
if secure:
    print("This link goes to a secure website!")
