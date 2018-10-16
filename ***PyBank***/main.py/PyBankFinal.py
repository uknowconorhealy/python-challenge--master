import csv
import os

profit_path = os.path.join("..", "desktop", "budget_data.csv")
absolute = "/Users/uknowconorhealy/Downloads/RUTJER201809DATA3-master 14/03-Python/Homework/Instructions/PyBank/Resources/budget_data.csv"

# variables
total_months = 0
prev_profit = 0
month_of_change = []
profit_change_list = []
greatest_increase = ["", 0]
greatest_decrease = ["", 9999999999999999999]
total = 0

with open(absolute) as profit_data:
    reader = csv.DictReader(profit_data)

    for row in reader:

        total_months = total_months + 1
        
        total = total + int(row["Profit/Losses"])

      
        profit_change = int(row["Profit/Losses"]) - prev_profit
        prev_profit = int(row["Profit/Losses"])
       
        profit_change_list = profit_change_list + [profit_change]
        
        month_of_change = month_of_change + [row["Date"]]

        if (profit_change > greatest_increase[1]):
            greatest_increase[0] = row["Date"]
            greatest_increase[1] = profit_change

        if (profit_change < greatest_decrease[1]):
            greatest_decrease[0] = row["Date"]
            greatest_decrease[1] = profit_change


profit_avg = sum(profit_change_list) / len(profit_change_list)


output = (
    f"\nFinancial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total Profit: ${total}\n"
    f"Average Profit Change: ${profit_avg}\n"
    f"Greatest Increase in Profit: {greatest_increase[0]} (${greatest_increase[1]})\n"
    f"Greatest Decrease in Profit: {greatest_decrease[0]} (${greatest_decrease[1]})\n")

print(output)

with open('budget_data_output.csv', "w") as new_file:
    new_file.write(output)