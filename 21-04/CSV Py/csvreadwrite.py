import csv

with open('DetailsPrint.csv','r') as csv_file:
    csv_reader = csv.reader(csv_file,delimiter='\t')
    with open('Details.csv','w') as csv_file:
        csv_writer = csv.writer(csv_file,delimiter='\t')

        for i in csv_reader:
            csv_writer.writerow(i)
