# Final Challenge:
# Print numbers from 1 to 30
# Skip numbers divisible by 3
# Stop if number > 25

for num in range(1, 31):
    if num > 25:
        break
    if num % 3 == 0:
        continue
    print(num)
