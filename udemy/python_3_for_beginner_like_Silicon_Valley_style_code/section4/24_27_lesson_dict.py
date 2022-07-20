d = {'x': 10, 'y': 20}
print(d, type(d))
print(d['x'], d['y'])

d['z'] = 200
print(d)

print(dict(a=10, b=20))

# 사전형의 메소드
d.get('xz') # 키가 없으면 NoneType
d['xz'] # 키가 없으면 KeyError

'''26. 사전형의 복사'''
x = {'a': 1}
y = x # 참조전달 
y['a'] = 1000
print(x, y) # 참조전달이기 때문에 값이 같음 

# 27. 사전형의 사용 예 
fruits = {
    'apple': 100,
    'banana': 200,
    'orange': 300,
}

print(fruits['apple'])