# JSON Parsing and Creation
import json

# 1. Convert Python dict to JSON
person = {
    "name": "Alice",
    "age": 22,
    "city": "New York"
}

json_str = json.dumps(person, indent=4)
print("JSON String:")
print(json_str)

# 2. Parse JSON to Python
parsed_data = json.loads(json_str)
print("Parsed Name:", parsed_data["name"])

# 3. Write JSON to file
with open("sample-data.json", "w") as f:
    json.dump(person, f, indent=4)

# 4. Read JSON from file
with open("sample-data.json", "r") as f:
    loaded_data = json.load(f)

print("Loaded from file:", loaded_data)