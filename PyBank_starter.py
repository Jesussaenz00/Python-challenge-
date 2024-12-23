import csv

# Initialize variables
months = []
profits_losses = []
changes = []

# Read the CSV file
with open('Resources/budget_data.csv', 'r') as file:
    csvreader = csv.reader(file)
    header = next(csvreader)  # Skip the header
    for row in csvreader:
        months.append(row[0])
        profits_losses.append(int(row[1]))

# Calculate the total number of months
total_months = len(months)

# Calculate the net total amount of "Profit/Losses" over the entire period
net_total = sum(profits_losses)

# Calculate the changes in "Profit/Losses" over the entire period
for i in range(1, total_months):
    change = profits_losses[i] - profits_losses[i - 1]
    changes.append(change)

# Calculate the average of those changes
average_change = sum(changes) / len(changes)

# Find the greatest increase in profits (date and amount)
greatest_increase = max(changes)
greatest_increase_month = months[changes.index(greatest_increase) + 1]

# Find the greatest decrease in profits (date and amount)
greatest_decrease = min(changes)
greatest_decrease_month = months[changes.index(greatest_decrease) + 1]

# Prepare the output string
output = (
    f"Total Months: {total_months}\n"
    f"Net Total: ${net_total}\n"
    f"Average Change: ${average_change:.2f}\n"
    f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})\n"
    f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})\n"
)

# Write the output to a text file
with open('Analysis/budget_analysis.txt', 'w') as output_file:
    output_file.write(output)

# Print the output to the terminal
print(output)