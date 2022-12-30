# Module 3 challenge - PyBank
# https://courses.bootcampspot.com/courses/2974/assignments/45813?module_item_id=845393

import os
import csv

csv_path = os.path.join('../PyBank','Resources', 'budget_data.csv')

# read CSV file
with open(csv_path) as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # read and print the header row
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    # read each row of data after the header
    # count number of months
    # net total amount of "Profit/Losses" over the entire period
    month_count = []
    total = []

    for row in csvreader:
        month_count.append(row[0])
        total.append(int(row[1]))

    # print(len(month_count))
    # print(sum(total))

    # sum and average of the changes in "Profit/Losses" over the entire period
    total_profit_loss = []
    for i in range (1, len(total)):
        profit_loss_change = total[i] - total[i-1]
        total_profit_loss.append(profit_loss_change)

    avg_change = (sum(total_profit_loss)/len(total_profit_loss))
    # print(round(avg_change, 2))

    # greatest increase in profits(date and amount) over the entire period
    greatest_profit = max(total_profit_loss)
    greatest_profit_month_index = total_profit_loss.index(greatest_profit)
    greatest_profit_month = month_count[greatest_profit_month_index+1]
    # print(greatest_profit, greatest_profit_month)

    # greatest decrease in profits(date and amount) over the entire period
    greatest_loss = min(total_profit_loss)
    greatest_loss_month_index = total_profit_loss.index(greatest_loss)
    greatest_loss_month = month_count[greatest_loss_month_index + 1]
    # print(greatest_loss, greatest_loss_month)

# print final analysis to the terminal
print("Financial Analysis")
print("----------------------------")
print(f"Total Months:  {len(month_count)}")
print(f"Total:  ${sum(total)}")
print(f"Average Change:  ${round(avg_change, 2)}")
print(f"Greatest Increase in Profits:  {greatest_profit_month} (${greatest_profit})")
print(f"Greatest Decrease in Losses:  {greatest_loss_month} (${greatest_loss})")
