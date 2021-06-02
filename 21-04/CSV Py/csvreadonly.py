import csv

with open('DetailsPrint.csv','r') as csv_file:
    csv_reader = csv.DictReader(csv_file,delimiter='\t')
    for line in csv_reader:
        print(line)
