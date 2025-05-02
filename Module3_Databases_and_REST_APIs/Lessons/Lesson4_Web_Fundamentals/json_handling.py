import json

# Example JSON string
person_json = """
{
    "name": "John",
    "age": 30,
    "skills": ["Python", "Data Analysis"]
}
"""

# Parse JSON
person = json.loads(person_json)
print(f"Name: {person['name']}, Skills: {person['skills']}")

# Convert Python object to JSON
person_dict = {"name": "Alice", "age": 25, "is_student": True}
json_output = json.dumps(person_dict)
print(json_output)
