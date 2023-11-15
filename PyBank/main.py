### First we'll import the os module
### This will allow us to create file paths across operating systems
import os

### Module for reading CSV files
import csv

csvpath = os.path.join('PyBank','Resources', 'budget_data.csv')

number_of_mth = 1
current_row = 0
prev_row = 0
current_net_profit_loss =  0
avg =0
net_profit_loss = []
total = 0
Total_profit_loss = 0
greatest_increase = 0
prev_greatest_increase= 0


current_greatest_decrease = 0 
prev_greatest_decrease = 0

with open(csvpath) as csvfile:

    ### CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    ### Read the header row first 
    csv_header = next(csvreader)

    ### Read the second row in csv file
    first_row = next(csvreader) 
    total += int(first_row[1]) 

    current_net_profit_loss = int(first_row[1])  
    prev_row = int(first_row[1]) 
    prev_greatest_increase_mth = (first_row[0])
    prev_greatest_decrease_mth = (first_row[0])
    
    ### Read each row of data after the 2nd row

    for row in csvreader:
        number_of_mth = number_of_mth + 1
        current_row = int(row[1])

        current_net_profit_loss = current_row - prev_row 
        current_greatest_increase = current_net_profit_loss
        current_greatest_increase_mth = row[0]
        current_greatest_decrease = current_net_profit_loss
       
        ### calculation for Greatest Increase in profits
        if current_greatest_increase > 0 and current_greatest_increase > prev_greatest_increase  :
            prev_greatest_increase = current_greatest_increase
            prev_greatest_increase_mth =   current_greatest_increase_mth           
        
        ### calculation for Greatest Decrease in profits

        if current_greatest_decrease < 0 and current_greatest_decrease < prev_greatest_decrease :
            prev_greatest_decrease = current_greatest_decrease
            prev_greatest_decrease_mth =   current_greatest_increase_mth
           
        net_profit_loss += [current_net_profit_loss]
        prev_row = current_row
        total += int(row[1])     
        avg = round(sum(net_profit_loss)/len(net_profit_loss),2)
    ### Printing the result/output on terminal
    print("Financial Ananlysis") 
    print("--------------------------------")
    print("Total Months :",number_of_mth)  
    print(f"Total : ${total}")
    print(f"Average Change : ${avg}")
    print(f"The Greatest Increase in Profits : { prev_greatest_increase_mth} (${prev_greatest_increase})")
    print(f"The Greatest Decrease in Profits : { prev_greatest_decrease_mth} (${prev_greatest_decrease})")
    
### Printing the result/output in text file
### Set variable for output file
output_file = os.path.join('PyBank','analysis','PyBankoutput.txt')

###  Open the output file
with open(output_file, "w") as outputfile:
    print("Financial Ananlysis",file=outputfile) 
    print("--------------------------------",file =outputfile)
    print("Total Months :",number_of_mth,file =outputfile)  
    print(f"Total : ${total}",file =outputfile)
    print(f"Average Change : ${avg}",file =outputfile)
    print(f"The Greatest Increase in Profits : { prev_greatest_increase_mth} (${prev_greatest_increase})",file =outputfile)
    print(f"The Greatest Decrease in Profits : { prev_greatest_decrease_mth} (${prev_greatest_decrease})",file =outputfile)
 