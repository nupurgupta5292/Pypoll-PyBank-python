# Importing essential modules
import os
import csv
import statistics

# Setting up path for file
csvpath = os.path.join("C:/Users/nites/Desktop/UT-TOR-DATA-PT-01-2020-U-C/03-Python/Instructions/PyBank/Resources","budget_data.csv")

# Empty list for storing names of months
month_name = []
# Empty list for storing the net total amount of "Profit/Losses" over the entire period
net_profit_loss = []
# Empty list for storing change in profit/loss
change_profit_loss = []

# Opening the CSV
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)

    # For loop for reading all rows in the CSV and adding them to specific lists
    for row in csvreader:

        month_name.append(row[0])
        net_profit_loss.append(int(row[1]))

    # Printing headers    
    print("Financial Analysis")
    print("----------------------------")

    # Printing number of months recorded
    print(f"Total Months : {len(month_name)}")

    # Printing net total amount of "Profit/Losses" over the entire period
    print(f"Total : ${str(sum(net_profit_loss))}")

    # Separate loop for calculating change in profit or loss
    for i in range(1,len(net_profit_loss)):

        # Stores change in profit or loss from one month to another in a list
        change_profit_loss.append(net_profit_loss[i] - net_profit_loss[i-1])
    
    # Calculating average of the changes in "Profit/Losses" over the entire period to two decimal places
    avg_change = round(float(statistics.mean(change_profit_loss)),2)

    # Calculating greatest increase and decrease in "Profit/Losses" over the entire period
    max_profit = max(change_profit_loss)
    max_loss = min(change_profit_loss)

    # Retrieving months with greatest increase and decrease in "Profit/Losses" over the entire period
    # Adjusting index by adding 1 to indicate correct month of change
    max_profit_month = str(month_name[change_profit_loss.index(max_profit)+1])
    max_loss_month = str(month_name[change_profit_loss.index(max_loss)+1])

    # Printing average of the changes in "Profit/Losses" over the entire period
    print(f"Average Change: ${str(avg_change)}")

    # Printing greatest increase in profits (date and amount) over the entire period
    print(f"Greatest Increase in Profits: {max_profit_month} (${str(max_profit)})")

    # Printing greatest decrease in losses (date and amount) over the entire period
    print(f"Greatest Decrease in Profits: {max_loss_month} (${str(max_loss)})")

# Exporting the output to a text file
output_file = open('C:/Users/nites/Desktop/python-challenge/PyBank/PyBank_output.txt', 'w')
output = "Financial Analysis\n----------------------------\nTotal Months : " + str(len(month_name)) + "\nTotal : $" + str(sum(net_profit_loss)) + "\nAverage Change: $" + str(avg_change) + "\nGreatest Increase in Profits: " + max_profit_month + " ($" + str(max_profit) + ")\nGreatest Decrease in Profits: " + max_loss_month + " ($" + str(max_loss) + ")"
output_file.write(output)
output_file.close()