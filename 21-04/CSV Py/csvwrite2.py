import csv

with open('demo2.csv',mode='w') as csvfile:
    writer=csv.writer(csvfile,delimiter=',',quotechar='"',quoting=csv.QUOTE_MINIMAL)

    writer.writerow(['CVR','College','Engineering'])
