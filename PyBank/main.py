import csv

path1 = '/Users/glena.dagger/Desktop/BootCamp/AssignmentRepositories/Python-Challenge/PyBank/Resources/budget_data.csv'

with open(path1, 'r') as file:
    reader = csv.reader(file)
    header = next(reader)

    month_count = 0
    total_profit = 0
    date_list = []
    profit_list = []
    max_profit = 0
    min_profit = 0
    

    for row in reader:
        
        # Increase number of months by 1 to keep track
        month_count += 1
        # Update total_profit variable by adding the value in the Profit column (and casting it as int)
        total_profit += int(row[1])


        if int(row[1]) > max_profit:
            max_profit = int(row[1])
            max_profit_date = row[0]
        
        if int(row[1]) < min_profit:
            min_profit = int(row[1])
            min_profit_date = row[0]

    
    avg_profit = total_profit / month_count



    print("Financial Analysis")
    print("----------------------------")
    print(f"Total Months: {month_count}")
    print(f"Total Profit: {total_profit}")
    print(f"Average Profit: {avg_profit}")
    print(f"Greatest Increase in Profits: {max_profit_date} {max_profit}")
    print(f"Greatest Decrease in Profits: {min_profit_date} {min_profit}")



with open('financial_analysis.txt', 'w') as out_file:
    writer = csv.writer(out_file)

    lines = ['Financial Analysis', '----------------------------', 'Total Profit: ' + str(total_profit), 'Average Profit: ' + str(avg_profit), 'Greatest Increase in Profits: ' + max_profit_date + ' ' + str(max_profit), 'Greatest Decrease in Profits: ' + min_profit_date + ' ' + str(min_profit)]

    for line in lines:
        out_file.write(line)
        out_file.write('\n')