import csv
import os

print("============================================================")
print("Hello, I am Roboko. What is your name?")
print("============================================================")

name = input()

FILE_PATH = os.path.join(os.path.dirname(os.path.realpath(__file__)))
# 선택 
with open(os.path.join(FILE_PATH, 'ranking.csv'), 'r') as csv_file:
    reader = csv.DictReader(csv_file)
    if reader.line_num > 1:
        for row in reader:
            print(f"추천해드리는 레스토랑은 {row['Name']} 입니다.")
            print(f'이 레스토랑을 좋아하세요? [Yes/No]')
            
            is_like = input()
            if is_like.upper() == 'Yes'.upper():
                pass
            

print(f'{name}씨, 좋아하는 레스토랑 이름은 무엇인가요?')
restaurant = input()

print(f'{name}씨, 감사합니다.')
print('좋은 하루 보내세요! 안녕히가세요')
