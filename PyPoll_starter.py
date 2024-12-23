import csv

# Initialize variables
total_votes = 0
candidates = {}
winner = ""
winner_votes = 0

# Read the CSV file
with open('/mnt/data/election_data.csv', 'r') as file:
    csvreader = csv.reader(file)
    header = next(csvreader)  # Skip the header
    for row in csvreader:
        total_votes += 1
        candidate = row[2]
        if candidate in candidates:
            candidates[candidate] += 1
        else:
            candidates[candidate] = 1

# Calculate the percentage of votes each candidate won and determine the winner
output_lines = []
for candidate, votes in candidates.items():
    percentage = (votes / total_votes) * 100
    output_lines.append(f"{candidate}: {percentage:.3f}% ({votes})")
    if votes > winner_votes:
        winner = candidate
        winner_votes = votes

# Prepare the output string
output = (
    f"Total Votes: {total_votes}\n"
    + "-"*30 + "\n"
    + "\n".join(output_lines) + "\n"
    + "-"*30 + "\n"
    + f"Winner: {winner}\n"
    + "-"*30 + "\n"
)

# Write the output to a text file
with open('/mnt/data/election_results.txt', 'w') as output_file:
    output_file.write(output)

# Print the output to the terminal
print(output)