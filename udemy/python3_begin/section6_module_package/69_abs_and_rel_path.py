# from section6.utils import utils
# import section6.utils.utils # 어떤 회사에서는 전체 이름을 불러오기도 하지만 사용시 이름이 너무 길어지는 단점이 있음  

from section6.utils import utils as u 
from section6.talk import human

# 상대path 파이썬에서 추천하지 않음 
# from ..section6.talk import human

print(human.sing())
