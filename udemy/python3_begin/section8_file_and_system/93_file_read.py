s = """\
AAA
BBB
CCC
DDD    
"""

with open('test.txt', 'r') as f:
    #1 한꺼번에 읽기 
    print(f.read()) 
    
    #2 한줄 씩 읽기
    while True:
        line = f.readline()
        # print(line, end='') # 줄 바꿈 X
        print(line) # 줄 바꿈 
        if not line:
            break
        
    #3 문자 두개씩 읽기 (네트워크 패킷 단위에서 사용할 수 있음)
    while True:
        chunk = 2
        line = f.read(chunk)
        print(line)
        if not line:
            break
        
        