import re

# Example 1: Count occurrences of 'and'
text = "Hi my name is Travis, and I like to go and do things and stuff"
ands = re.findall(r"and", text)
print("Occurrences of 'and':", ands)
print("Count:", len(ands))

# Example 2: Extract hashtags from a post
post = "I LOVE # learning #Python_is_lyfe and #Regex, this is so fun! #Code"
tags = re.findall(r"#\w+", post)
print("Hashtags found:", tags)

# Exercise: Extract hashtags from tweets
tweets = [
    "Loving the #sunset! So peaceful #nature #blessed",
    "Had a great day! #happy #friends #goodvibes",
    "Can't wait for the #weekend! #fun #relax"
]

for tweet in tweets:
    hashtags = re.findall(r"#\w+", tweet)
    print("Tweet:", tweet)
    print("Hashtags:", hashtags)
