import csv
import json
import jsonschema

# Define input schema
input_schema = {
    "type": "array",
    "items": {
        "type": "object",
        "properties": {
            "Name": {"type": "string"},
            "Number": {"type": "integer"},
        },
        "required": ["Name", "Number"],
    },
}

# Define output schema
output_schema = {
    "type": "array",
    "items": {
        "type": "object",
        "properties": {
            "Name": {"type": "string"},
            "Number": {"type": "integer"},
            "IsArmstrong": {"type": "boolean"},
            "IsStrong": {"type": "boolean"},
            "IsPerfect": {"type": "boolean"},
        },
        "required": ["Name", "Number", "IsArmstrong", "IsStrong", "IsPerfect"],
    },
}

# Function to check if a number is Armstrong
def is_armstrong(number):
    return number == sum(int(digit) ** len(str(number)) for digit in str(number))

# Function to check if a number is Strong
def is_strong(number):
    def factorial(n):
        return 1 if n == 0 else n * factorial(n - 1)
    return number == sum(factorial(int(digit)) for digit in str(number))

# Function to check if a number is Perfect
def is_perfect(number):
    divisors = [i for i in range(1, number) if number % i == 0]
    return number == sum(divisors)

# Read and parse the input CSV file
names = []
numbers = []

with open('input.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        names.append(row['Name'])
        numbers.append(int(row['Number']))

# Process data and create output
output_data = []

for name, number in zip(names, numbers):
    output_entry = {
        "Name": name,
        "Number": number,
        "IsArmstrong": is_armstrong(number),
        "IsStrong": is_strong(number),
        "IsPerfect": is_perfect(number)
    }
    output_data.append(output_entry)

# Write output data to a JSON file
with open('output.json', 'w') as json_file:
    json.dump(output_data, json_file, indent=4)

# Validate input data against input schema
try:
    jsonschema.validate(output_data, output_schema)
    print("Input data is valid.")
except jsonschema.ValidationError as e:
    print("Input data is not valid:", e)

# Validate output data against output schema
try:
    jsonschema.validate(output_data, output_schema)
    print("Output data is valid.")
except jsonschema.ValidationError as e:
    print("Output data is not valid:", e)
