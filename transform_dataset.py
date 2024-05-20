import json
import time
import uuid

# Start the timer
start_time = time.time()

# Load the dataset
with open('test.json', 'r') as f:
    data = json.load(f)

# Initialize a list to hold the formatted data
formatted_data = []

# Function to parse questions and answers
def parse_entry(entry):
    pairs = []
    lines = entry.split('. ')
    for line in lines:
        if '?' in line:
            question, answer = line.split('?', 1)
            pairs.append({
                "id": str(uuid.uuid4()),
                "Question": question.strip() + '?',
                "Answer": answer.strip()
            })
    return pairs

# Iterate through each entry in the dataset
for entry in data:
    input_text = entry['input']
    pairs = parse_entry(input_text)
    formatted_data.extend(pairs)

# Save the formatted data to a JSON file
with open('formatted_data.json', 'w') as f:
    json.dump(formatted_data, f, indent=2)

# Stop the timer
end_time = time.time()

# Report statistics
total_pairs = len(formatted_data)
time_taken = end_time - start_time

print(f'Total question-answer pairs extracted: {total_pairs}')
print(f'Time taken for dataset transformation: {time_taken} seconds')

