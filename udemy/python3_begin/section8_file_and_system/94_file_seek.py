s = """\
AAA
BBB
CCC
DDD    
"""

with open('test.txt', 'r') as f:
    print(f.tell()) # prt:0 
    print(f.read(1)) # prt:A
    f.seek(5) #prt: B (줄바꿈 갯수에 포함)
    #※파일의 끝에 다다르면 원래대로 다시 돌아감 
    
    
        