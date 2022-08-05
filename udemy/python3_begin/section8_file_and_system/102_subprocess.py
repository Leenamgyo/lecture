import os
from re import sub
from select import POLLOUT
import subprocess # 터미널에서 하는 것을 파이썬에서 하는 것 

os.system('ls') # 같은 기능인데 옛날 방식
subprocess.run(['ls']) # 요즘 방식, 높은 기능을 가짐 
subprocess.run(['ls' '-al'])
subprocess.run('ls -al', shell=True) # shell에 넘겨줘서 실행 가능, shell injection을 일어나 해킹의 가능성이 있기 때문에 사용 권장 X

r= subprocess.run('lsa', shell=True) # 에러가 발생하지 않음, 다만 r.returncode가 0이아닌 이상한 결과값이 나옴
print(r.returncode) 
r= subprocess.run('lsa', shell=True, check=True) # 실행시 커멘드 에러가 날 경우 터미널 출력 후 interrupt


# 쉘 인젝션을 피하는 방법, 리눅스를 잘 아는 사람만 사용할 것 
p1 = subprocess.Popen(['ls', '-al'], stdout=subprocess.PIPE)
p2 = subprocess.Popen(['ls', '-al'], stdin=p1.stdout, stdout=subprocess.PIPE)

p1.stdout.close()
output = p2.communicate()[0]
print(output)
