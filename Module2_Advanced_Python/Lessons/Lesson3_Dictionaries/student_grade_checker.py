# Final Challenge: Student pass/fail checker

students = {
    'Alice': 85,
    'Bob': 42,
    'Charlie': 68,
    'David': 49
}

# Loop through and print result
for student, grade in students.items():
    status = "passed" if grade >= 50 else "failed"
    print(f"{student} {status}.")
