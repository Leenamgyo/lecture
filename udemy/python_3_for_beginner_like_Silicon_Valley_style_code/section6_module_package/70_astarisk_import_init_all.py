# 직접 선언 방법
# from section6.talk import human
# from section6.talk import animal

# print(animal.sing())
# print(animal.cry())

# '*' 사용방법
# 어떤 역할이 쓰였는지 찾기 힘들기 때문에 추천하지 않습니다. 
from section6.talk import *

print(animal.sing())
print(animal.cry())