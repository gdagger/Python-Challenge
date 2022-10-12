##  MODULE 3 HOMEWORK
##  PyBank
##  Glen Dagger

# Import csv module for reading csv file
import csv

# Import path from os module to designate file path
from os import path


## VARIABLES

# Initialize month_count variable to 0 to track total month count (number of rows)
month_count = 0

# Create empty list to store profits
profit_list = []

# Create empty list to store dates
date_list = []

# Initialize total_profit variable to 0 to track total profit
total_profit = 0


## READ DATA FROM CSV FILE

# Store csv file path for 'budget_data.csv' in csvpath variable
csvpath = path.join('..','PyBank','Resources','budget_data.csv')

# Open budget_data.csv to read data
with open(csvpath, 'r') as file:

    # Create reader object to iterate through data
    reader = csv.reader(file)

    # Store header so For loop begins on first data row
    header = next(reader)

    ## FOR LOOP
    # Iterate through each row of budget_data.csv to collect relevant data from each row
    for row in reader:
        
        # Increase number of months by 1 to keep track of running total
        month_count += 1

        # Append profit/loss from current row to profit_list
        profit_list.append(int(row[1]))

        # Append date from current row to list of dates
        date_list.append(row[0])

        # Update total_profit variable by adding the value in the Profit column (and casting it as int)
        total_profit += int(row[1])
    ## END FOR LOOP


## DATA ANALYSIS

# List comprehension to create new list consting of the changes in profit from each month to the next
profit_changes = [(profit_list[i+1] - profit_list[i]) for i in range(len(profit_list)-1)]

# Slice list of dates to exclude starting date and store in new list (equal in size to profit_changes list)
date_changes = date_list[1:]

# Dictionary Comprehension to include each date as KEY and corresponding change in profit as VALUE
profit_changes_dict = {date_changes[i]:profit_changes[i] for i in range(len(date_changes))}

# Calculate average change in profit by summing elements in profit_changes and dividing by the total number of elements (rounded to 2 decimal places)
avg_profit_change = round((sum(profit_changes) / len(profit_changes)),2)


# Find MAX value in profit_changes_dict and store in variable
max_profit = max(profit_changes_dict.values())

# List comprehension to collect all dates that match MAX profit change value in profit_changes_dict (just in case there are more than one)
max_profit_dates = [k for k,v in profit_changes_dict.items() if v == max_profit]

# Find MIN value in profit_changes_dict and store in variable
min_profit = min(profit_changes_dict.values())

# List comprehension to collect all dates that match MIN profit change value in profit_changes_dict (just in case there are more than one)
min_profit_dates = [k for k,v in profit_changes_dict.items() if v == min_profit]



### FINANCIAL ANALYSIS

# Create list with financial analysis information to print to terminal/write to outgoing file
financial_analysis = ["\nFinancial Analysis",
                    "----------------------------",
                    f"Total Months: {month_count}",
                    f"Total Profit: ${total_profit}",
                    f"Average Change in Profit: ${avg_profit_change}",
                    f"Greatest Increase in Profits: {','.join([x for x in max_profit_dates])} (${max_profit})",
                    f"Greatest Decrease in Profits: {','.join([x for x in min_profit_dates])} (${min_profit})\n"]

## PRINT IN TERMINAL
# Print financial analysis data in terminal
print('\n\n'.join(financial_analysis))


## WRITE TO OUTGOING TEXT FILE

# Store file path for outgoing text file
out_path = path.join('..','PyBank','Analysis','financial_analysis.txt')

# Open outgoing text file to write financial analysis
with open(out_path, 'w', newline='') as out_file:

    # Create writer object to write financial analysis to outgoing text file
    writer = csv.writer(out_file)

    # Write items in financial_analysis to outgoing text file separated by new lines
    out_file.write('\n\n'.join(financial_analysis))