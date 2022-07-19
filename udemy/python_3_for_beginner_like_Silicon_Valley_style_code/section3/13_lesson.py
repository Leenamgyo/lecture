'''문자의 메소드'''
s = 'My name is Mike. Hi Mike.'
is_start = s.startswith('My')
print(is_start) # True
is_start = s.startswith('X')
print(is_start)

print("##################")

print(s.find('Mike'))
print(s.rfind('Mike')) # 뒤에서 계산해서 찾아줌
print(s.count('Mike'))
print(s.capitalize()) # 앞 글자 대문자
print(s.title())
