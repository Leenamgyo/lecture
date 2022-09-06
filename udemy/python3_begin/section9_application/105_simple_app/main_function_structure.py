""" 
    program for recommnding restaurant
    
    1. 이름을 입력받는다.
    2. 추천 받은 레스토랑의 호감도를 좋아한다.
    3. 레스토랑을 추천받는다.
    
"""

import csv
from enum import Enum
import os
from pkgutil import get_data
from typing import Dict

ANSWER_YES = "YES"
ANSWER_NO = "NO"
FILE_NAME = "ranking.csv"
FILE_PATH = os.path.join(os.path.dirname(os.path.realpath(__file__)))
CSV_FILE_NAME = "Name"
CSV_FILE_COUNT = "Count"
FIELD_NAMES = [CSV_FILE_NAME, CSV_FILE_COUNT]
    

def input_name() -> str:
    """
        사용자의 이름을 등록합니다.
    """
    
    while True:
        try:
            name = input()
            if not name.isalpha():
                raise ValueError("Names can only be written in English")
        except ValueError as e:
            continue
            
        return name

def survey_the_prefs():
    """
        파일에 등록된 데이터 목록 중 
        좋아하는 데이터의 선호도를 올립니다.  
    """
    
    csv_data = get_csv()
    rows = csv_data["rows"]
            
    for row in rows:
        print(f"추천해드리는 레스토랑은 {row[CSV_FILE_NAME]} 입니다.")
        print(f'이 레스토랑을 좋아하세요? [Yes/No]')
                
        is_like = input()
        if is_like.upper() == ANSWER_YES.upper():
            row[CSV_FILE_COUNT] = str(int(row[CSV_FILE_COUNT]) + 1)
        
    insert(csv_data)

    
def register_the_prefs(name):
    """
        목록에 데이터를 등록합니다. 
    """
    csv_data = get_csv()
    rows = csv_data["rows"]
    
    print(f'{name}씨, 좋아하는 레스토랑 이름은 무엇인가요?')
    restaurant_name = input()
    
    is_exist = False
    for row in rows:
        if restaurant_name == row[CSV_FILE_NAME]:
            is_exist = True
            row[CSV_FILE_COUNT] = str(int(row[CSV_FILE_COUNT]) + 1)
    
    if not is_exist:
        rows.append(
            {
                CSV_FILE_NAME: restaurant_name,
                CSV_FILE_COUNT: "1"
            }
        )
    
    insert(csv_data)
    

def get_csv() -> dict[str, list]:
    """
        데이터 목록을 가져옵니다.
    """
    csv_data = None
    with open(os.path.join(FILE_PATH, FILE_NAME), mode='r') as csv_file:
        reader = csv.DictReader(csv_file)
        csv_data = {
            "header": reader.fieldnames,
            "rows": [
                {   
                    CSV_FILE_NAME: row[CSV_FILE_NAME],
                    CSV_FILE_COUNT: row[CSV_FILE_COUNT]
                 } 
                for row in reader
            ]
        }
                
    return csv_data
        
def check_file_exist():
    """
        파일의 존재 유무 및 유효성 검증을 체크합니다.
        만약, 
    """
    try:
        with open(os.path.join(FILE_PATH, FILE_NAME), mode='r') as csv_file:
            reader = csv.DictReader(csv_file)
            
            # File Header Check
            for idx in range(len(FIELD_NAMES)):
                if reader.fieldnames[idx] != FIELD_NAMES[idx]:
                    raise FileNotFoundError()
                                
    except FileNotFoundError as err:
        create_file()
 
def create_file():
    with open(os.path.join(FILE_PATH, FILE_NAME), mode='w') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=FIELD_NAMES)
        writer.writeheader()

def insert(csv_data):
    """ 데이터를 삽입합니다.

    Args:
        list_data (_type_): 목록 데이터 
    """
    with open(os.path.join(FILE_PATH, FILE_NAME), mode='w') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=csv_data["header"])
        writer.writeheader()
        
        for row in csv_data["rows"]:
            writer.writerow(
                {
                    CSV_FILE_NAME: row[CSV_FILE_NAME], 
                    CSV_FILE_COUNT: row[CSV_FILE_COUNT]
                }
            )

    
if __name__ == '__main__':
    print("============================================================")
    print("Hello, I am Roboko. What is your name? (Press Ctrl+C to exit the program)")
    print("============================================================")
    
    try:
        check_file_exist()
        
        name = input_name()
        survey_the_prefs()
        register_the_prefs(name=name)
    except KeyboardInterrupt as e:
        print('exit the program')
        quit()
        
    print(f'{name}씨, 감사합니다.')
    print('좋은 하루 보내세요! 안녕히가세요')
 