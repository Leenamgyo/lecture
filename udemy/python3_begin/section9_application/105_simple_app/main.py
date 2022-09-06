import csv
from enum import Enum
import os

ANSWER_YES = 'YES'
ANSWER_NO = 'NO'
FILE_NAME = 'ranking.csv'

class CsvField(Enum):
    NAME = 'Name'
    COUNT = 'Count'

FILE_PATH = os.path.join(os.path.dirname(os.path.realpath(__file__)))

print("============================================================")
print("Hello, I am Roboko. What is your name?")
print("============================================================")

name = input()

# 선택 
try:
    with open(os.path.join(FILE_PATH, FILE_NAME), mode='r+') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            print(f"추천해드리는 레스토랑은 {row[CsvField.NAME.value]} 입니다.")
            print(f'이 레스토랑을 좋아하세요? [Yes/No]')
            
            is_like = input()
            if is_like.upper() == ANSWER_YES.upper():
                writer = csv.DictWriter(csv_file, fieldnames=[field.value for field in CsvField])
                writer.writerow({CsvField.NAME.value: row[CsvField.NAME.value], CsvField.COUNT.value: str(int(row[CsvField.COUNT.value]) + 1)})
                
except FileNotFoundError as err:
    with open(os.path.join(FILE_PATH, FILE_NAME), mode='w') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=[field.value for field in CsvField])
        writer.writeheader()
    
    

print(f'{name}씨, 좋아하는 레스토랑 이름은 무엇인가요?')
restaurant = input()

with open(os.path.join(FILE_PATH, FILE_NAME), mode='a') as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=[field.value for field in CsvField])
    writer.writerow({CsvField.NAME.value: restaurant, CsvField.COUNT.value: 1})

print(f'{name}씨, 감사합니다.')
print('좋은 하루 보내세요! 안녕히가세요')
 



#1. recommand restrauant
# if yes/no 
#   yes == count +1
#   no or else == Nothing

#2. 좋아하는 레스토랑 질문

# 인사 


