# Import dependencies, create file path to csv file, and create average function.
import os
import csv
bankcsvpath = os.path.join("Resources", "budget_data.csv")
def average(numbers):
    return sum(numbers)/len(numbers)

# Open csv as reader, read through rows and run for loops to capture months and profits/losses in lists.
with open(bankcsvpath) as bankcsvfile:
    bankcsvreader = csv.reader(bankcsvfile, delimiter=",")
    bankcsvreader_header = next(bankcsvreader)  
    monthlist = []
    monthlymoneylist =[]
    mtmchangelist = []
    net_total = 0
    for row in bankcsvreader:
        monthlist.append(row[0])
        monthlymoney = float(row[1])
        monthlymoneylist.append(monthlymoney)
        net_total += monthlymoney
# Run for loop through money list to calculate change between months and greatest increase and decrease.
    i = 0
    greatest_increase = 0
    greatest_decrease = 0
    for currentmoney in monthlymoneylist:
        if i != len(monthlymoneylist) - 1:
            mtm_change = monthlymoneylist[i + 1] - monthlymoneylist[i]
            mtmchangelist.append(mtm_change)
            if monthlymoneylist[i] > greatest_increase:
                greatest_increase = monthlymoneylist[i]
                greatest_month = monthlist[i]
            if monthlymoneylist[i] < greatest_decrease:
                greatest_decrease = monthlymoneylist[i]
                worst_month = monthlist[i]
        i = i + 1
    mtmaverage = average(mtmchangelist)
    monthcount = len(monthlist)

# Create output file, print results to terminal, and write results to output file.
output_file = os.path.join("Analysis", "financial_analysis.txt")
with open(output_file,"w", newline="") as datafile: 
    writer = csv.writer(datafile)
    print("Financial Analysis")
    writer.writerow(["Financial Analysis"])
    print("-----------------------------")
    writer.writerow(["-----------------------------"])
    print(f"Total Months: {monthcount}")
    writer.writerow([f"Total Months: {monthcount}"])
    print(f"Total: ${int(net_total)}")
    writer.writerow([f"Total: ${int(net_total)}"])
    print(f"Average Change: ${round(mtmaverage,2)}")
    writer.writerow([f"Average Change: ${round(mtmaverage,2)}"])
    print(f"Greatest Increase in Profits: {greatest_month} (${int(greatest_increase)})")
    writer.writerow([f"Greatest Increase in Profits: {greatest_month} (${int(greatest_increase)})"])
    print(f"Greatest Decrease in Profits: {worst_month} (${int(greatest_decrease)})")
    writer.writerow([f"Greatest Decrease in Profits: {worst_month} (${int(greatest_decrease)})"])
