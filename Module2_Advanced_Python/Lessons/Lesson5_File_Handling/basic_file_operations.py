# Write and append to file
file = open('new_file.txt', 'w')
file.write('Writing to a file from Python!\n')
file.close()

file = open('new_file.txt', 'a')
file.write('Adding more content with "a" mode\n')
file.close()

# Read the file
with open('new_file.txt', 'r') as file:
    content = file.read()
    print("File contents:\n", content)
