# Original string with extra whitespace
my_string = '            Coding temple is the best bootcamp ever!      '

# 1. Convert to uppercase
upper_case = my_string.upper()
print("Uppercase:", upper_case)

# 2. Strip leading and trailing whitespace
stripped = my_string.strip()
print("Stripped:", stripped)

# 3. Replace a word in the sentence
replaced = stripped.replace("best", "greatest")
print("Replaced:", replaced)

# 4. Split the sentence into a list of words
words = replaced.split()
print("Split into words:", words)
