# 파이썬의 type 선언: 타입 추론 방식
num = 1
name = 'Mike'
is_ok = True

# 파이썬의 타입 확인: type(var) 내장 메소드를 사용 
print(num, type(num))
print(name, type(name))
print(is_ok, type(is_ok))

# 파이썬의 타입 변환 
num_str = '1'
num_num = int(num_str)

# 파이썬 type Hint 
num: int  = 1
name: str = '1'

# print 문구 
# sep = seperate, 기본 값은 space(' ')
# end를 설정하여 print출력 문구가 끝난 다음 동작을 지정할 수 있다, 기본 값은 '\n'
print('Hi', 'Mike', sep=",", end='\n') 

# 연산 
# +, -, *, /, //, %, **
print(17 // 3) # 소수점 출력하지 않음 
print(17 % 3) # 나머지만 출력 
print(5**5) # 제곱 

# 반올림 
pie = 3.141515151515
print(round(pie, 2)) # 수, 자리수 

# 수학 함수 
import math 
result = math.sqrt(25)
print(result) # 제곱근 

y = math.log2(10)
print(y) # 로그함수

# document 출력, help 함수 
# print(help(math)) 


########### 11. 문자열부터 #####################
print('hello')
print("hello")
print("I don't know")
print('I don\'t know')
print('hello. \nHow are you?')
print(r'C:\name\name') # r을 안쓰면 \n을 new line으로 인식합니다.

# """문자열""" > 여러 줄 출력, 엔터(\n)도 인식하며 엔터를 인식하고 싶지 않으면 \를 작성한다. 
print("""\
line1     
line2
line3\
""")

# 문자열 곱하기 
print('Hi.' * 3 + 'Mike.')
print('Py''thon')

s = ('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
     'bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb')

print(s)

# 12. 문자열과 슬라이스 
word = 'python'
print(word[0])
print(word[-2])

## 인덱스가 없을 경우 
# IndexError: string index out of range
print(word[100])

## 문자열을 바꾸고 싶은 경우

# 에러 1: TypeError: 'str' object does not support item assignment
word[0]= 'j'

# 바꾸는 방법
word = 'j' + word[1:]
