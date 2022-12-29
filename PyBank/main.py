# Import OS
import os

# import csv file
import csv


csvpath = os.path.join('C:\\Users\\cghos\\python-challenge\\PyBank', 'Resources', 'budget_data.csv')
print(csvpath)

# reading CSV file
with open(csvpath) as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    #print(csvreader)


    # Read the header row first
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    #row_count=0
    #total_rows=0
    month_count = []
    total = []


    # Read each row of data after the header
    # Count number of rows
    for row in csvreader:
        month_count.append(row[0])
        total.append(int(row[1]))


    print(len(month_count))
    print(sum(total))
    print()


