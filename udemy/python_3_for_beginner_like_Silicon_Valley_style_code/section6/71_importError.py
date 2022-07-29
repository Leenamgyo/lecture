from ast import Import
from section6.utils import utils

try:
    # 패키지 관리시 사용
    # 옛 버전이 위로 가게끔 
    from section6 import utils
    
except ImportError:
    from section6.talk import utils
    
utils.say_twice('word')