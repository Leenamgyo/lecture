from xxlimited import Xxo


a = 1
b = 1


a == b

a != b

a < b

a > b

a <= b

a >= b

a > 0 and b > 0

a > 0 or b > 0

"""in 과 not"""

y = [1, 2, 3]
x = 1

if x in y:
    print('in')
    
if 100 not in y:
    print('not in')
    
a = 1
b = 2

if not a == b:
    print('Not equal')
    
# not

is_ok =  True

if is_ok == True:
    print('Hello')
    
# 숫자 비교에서는 not을 많이 사용하지 않음 
# not을 쓰는 경우
if not is_ok:
    print('Hello')
    
# 파이썬의 숫자 
is_exists = 0 # False
is_exists = 1 # 만약 0보다 클 경우 True 

# 파이썬의 문자
is_exists = ''
is_exists = '123'

if is_exists:
    print('OK!')
else:
    print('No!')

# False 판정 
# False, 0, 0.0, '', [], (), {}, set()
