import csv

with open('demo.csv',mode='w') as csvfile:
    fieldnames=['name','dept','dob']
    writer=csv.DictWriter(csvfile,fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow({'name':'cvr','dept':'cse','dob':'june'})
