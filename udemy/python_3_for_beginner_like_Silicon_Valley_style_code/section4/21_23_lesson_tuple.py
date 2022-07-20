t = (1, 2, 3, 4, 1, 2)
type(t)

t[0] = 100 # tuple에 값을 넣는 것은 지원이 안됨, TypeError
t.index(1) # 0
t.index(1, 1) # 4
t.count(1) # 2

help(tuple) # 데이터 조작을 할 수는 없으니 데이터 읽기에 사용됨 
t = ([1,2,3], [4,5,6])
# t[0] = t[1], 튜플 조작시 Error 발생 

'''튜플의 언패킹'''
num_tuple = (10, 20)
print(num_tuple)

x, y = num_tuple
print(x, y)
# x, y = (10, 20)과 동일 

min, max = 0, 100
print(min, max)

a, b, c, d, e, f = 'Mike', '1', '1', '1', 'e', 'f'
a = 'Mike'
b = '1'

i = 10
j = 20
tmp = i 
i = j
j = tmp

print(i, j)

a = 100
b = 200

a, b = b, a # 변수의 수치를 바꾸는 것이 가능함 
print(a, b)


'''튜플의 예시'''
# 변환하기 곤란한 어플리케이션에는 리스트보다는 튜플사용할 것 
choose_from_two = ('A', 'B', 'C')

answer = []
answer.append('A')
answer.append('C')

print(choose_from_two)
print(answer)

