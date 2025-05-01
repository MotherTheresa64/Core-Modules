import re

# Splitting based on multiple delimiters
text = 'Python,Regex;Splitting-Example. Fun, right!'
words = re.split(r"[,.;\s\-!]+", text)
print("Words:", words)

# Substituting: Clean phone number
number = "(770) 888-1180"
cleaned = re.sub(r"\D", '', number)
print("Cleaned phone number:", cleaned)

# Substituting: Anonymize usernames
chat = '''
@Yve-bee123 : "I think I love Regex"
@Travis : "Aren't you married?"
@Yve_bee123 : "It's just not the same"
@Travis : "They better not see this!"
'''
anon_chat = re.sub(r"@[\w-]+", "@user-anon", chat)
print("Anonymized chat:\n", anon_chat)
