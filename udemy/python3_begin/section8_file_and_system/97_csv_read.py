import csv
import os

FILE_PATH = os.path.join(os.path.dirname(os.path.realpath(__file__)))

with open(os.path.join(FILE_PATH, 'file','text.csv'), 'w') as csv_file:
    fieldnames = ['Name', 'Count']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    
    writer.writerow({'Name':'A', 'Count': 1})
    writer.writerow({'Name':'B', 'Count': 2})
    
# 선택 
with open('test.csv', 'r') as csv_file:
    reader = csv.DictReader(csv_file)
    for row in reader:
        print(row['Name'], row['Count'])