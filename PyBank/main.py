# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')

months = []
total_profit = []
monthly_change = []

with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader, None)
    for row in (csvreader):
        #puts months in a list so that later I'm able to figure out the count using the LEN function
        months.append(row[0])
  
        #puts profit column in a list and must change to INT so that I can later use the SUM function
        total_profit.append(int(row[1]))

        # gets range of 0, 85 to iterate through list of total_profit
    for i in range(len(total_profit)-1):
        
        #iterates through grabs the next total profit and subtracts from the one previous and begins putting that in a list to show the monthly change, that why we only want
        #85 in range, the final subtraction is row 86-85 
        monthly_change.append(total_profit[i+1]-total_profit[i])

#couldn't figure out how to reference corresponding month to the max increase and min decrease

print("Financial Analysis")
print("-----------------------------------------------------------")
print (f"Total Months: {len(months)}")
print(f"Total: ${sum(total_profit)}")
print(f"Average change: {round(sum(monthly_change)/len(monthly_change),2)}")
print(f"Greatest increase in profits: ${max(monthly_change)}")
print(f"Greatest decrease in profies: ${min(monthly_change)}")

# Specify the file to write to
output_path = os.path.join("Analysis", "financial_analysis.txt")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w') as file:

        # Write the first row (column headers)
    file.write("Financial Analysis \n")
    file.write("-------------------------------------------------------\n")
    file.write(f"Total Months: {len(months)}\n")
    file.write(f"Total: ${sum(total_profit)}\n")
    file.write(f"Average change: {round(sum(monthly_change)/len(monthly_change),2)}")
    file.write(f"Greatest increase in profits: ${max(monthly_change)}\n")
    file.write(f"Greatest decrease in profies: ${min(monthly_change)}\n")


    