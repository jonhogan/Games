import json
import os

# Define the input and output file names
input_file = "citiesWorld.json"
output_file = "citiesWorldCleaned.json"

# Try opening the file with different encodings until successful
encodings = ["utf-8", "cp1252", "iso-8859-1"]
for encoding in encodings:
    try:
        with open(input_file, "r", encoding=encoding) as f:
            data = json.load(f)
        break
    except UnicodeDecodeError:
        continue

# Remove duplicates from the data
unique_data = [dict(t) for t in {tuple(city.items()) for city in data}]

# Save the unique data to the output file using the utf-8 encoding
with open(output_file, "w", encoding="utf-8") as f:
    json.dump(unique_data, f, indent=4, ensure_ascii=False)