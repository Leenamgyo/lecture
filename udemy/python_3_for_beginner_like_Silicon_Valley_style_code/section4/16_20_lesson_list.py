'''16강 리스트형'''
# 슬라이싱, offset, 인덱스 가능 
# 리스트 안에 자료형은 아무거나 넣을 수 있음 
l = [1, 20, 4, 50, 2, 1, 2]
print(len(l), type(l))

# print(l[100]) IndexError

'''17강 리스트의 조작'''
# 리스트 변수 접근 
s = ['a','b','c','d','e']
s [0] = 'X' # 문자열과 다르게 가능하다. 
s.append('y') # index의 끝에 y를 추가한다.
s.insert(0, 'A') # 0번째 index에 A를 넣어라
s.pop() # defualt는 마지막 index, index에 있는 값을 꺼내고 출력하라
del s[0] # index의 변수를 삭제할 것 
s.remove('b') # 앞에서부터 차례대로 확인해서 이에 해당하는 변수를 지워줌, 변수가 존재하지 않으면 ValueError가 됨 

b = [1,2,3,4,5] 
# 리스트의 병합은 +로 한다. 
x = s + b 

# 병합 후 할당 
s +=b
s.extend(b)

'''18강 리스트의 메서드'''
r = [1,2,3,4,5,1,2,3]
print(r.index(3)) # 원소의 index에 접근하여 index 값을 리턴 
print(r.index(3, 3)) # 4번째 원소부터 찾는다. 원소의 index에 접근하여 index 값을 리턴 
print(r.count(3)) # 원소 3의 개수 리턴 

if 5 in r:
    print('exist')
    
r.sort() # sorting 
print(r)
r.sort(reverse=True) # 꺼꾸로
print(r)
r.reverse()
print(r)

s = 'My name is Mike'
to_split = s.split(' ')
print(to_split)

x = ' '.join(to_split)
print(x)

x = '#####'.join(to_split)
print(x)

print(help(list))

'''19. 리스트의 복사'''
i = [1, 2, 3, 4, 5]
j = i
print('j=', j)
print('i=', i)

x = [1, 2, 3, 4, 5]
# y = x.copy()
y = x[:] # y랑 x가 같음
y[0] = 100
print('y=', y)
print('x=', x)

print(id(x), id(y)) #서로간의 주소가 다름

'''20. 리스트의 사용 예'''
seat = []
min = 0
max = 5

# 손님을 계속해서 추가시켰을 경우 min/max를 판별하여 seat의 값을 리턴시켜 줌 
min <= len(seat) < max

