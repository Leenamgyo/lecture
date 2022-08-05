s = """\
AAA
BBB
CCC
ZZZ    
"""

#1 w+ 모드 
# w+ 모드는 파일 초기화 후 write (read 가능)
# with open('test.txt', 'w+') as f:
#     f.write(s)
#     f.seek(0) # 처음으로 돌아가야 함
#     print(f.read())
    

#1 r+ 모드 
# r+ 모드는 파일 읽기 후 write (read 가능)
with open('test.txt', 'r+') as f:
    f.write(s) # 파일 초기화 후 작성 
    f.seek(0) # 처음으로 돌아가야 함
    print(f.read()) 
    
        