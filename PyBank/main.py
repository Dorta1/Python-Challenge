#Import modules
import os
import csv

#Set variables
total_months=0
net_total=0
net_previous=0
changes_list=[]
greatest_increase=["",0]
greatest_decrease=["",9999999999999]

#Set file paths
input_file = os.path.join("c:","budget_data.csv")
output_file = os.path.join("Financial_Analysis.txt")

#Open file and create reader
with open(input_file, "r", newline="") as csvfile:
    reader=csv.reader(csvfile, delimiter=",")
    
    #Header
    header= next(reader)
    
    first_row= next(reader)
    total_months+=1
    net_total= net_total + int(first_row[1])
    net_previous=int(first_row[1])

    for row in reader:
        total_months+=1
        net_total= net_total + int(row[1])

        changes= int(row[1]) - net_previous
        changes_list.append(changes)

        if changes > greatest_increase[1]:

            greatest_increase[0]= row[0]
            greatest_increase[1]= changes

        if changes < greatest_decrease[1]:
            greatest_decrease[0]= row[0]
            greatest_decrease[1]=changes

    avg_changes=sum(changes_list)/len(changes_list)

output= (
    f'\nFinancial Analysis\n'
    f'-------------------------------------------------\n'
    f'Total Months: {total_months}\n'
    f'Total: ${net_total}\n'
    f'Average of the changes: ${avg_changes}\n'
    f'Greatest increase: ${greatest_increase[1]} on {greatest_increase[0]}\n'
    f'Greatest decrease: ${greatest_decrease[1]} on {greatest_decrease[0]}\n'
    f'--------------------------------------------------')

print(output)

with open(output_file, 'w') as txt_file:
    txt_file.write(output)



