"""28. 집합형이란"""
a = {6, 1, 2, 2, 3, 4, 4, 4, 5, }
b = {2, 3, 6, 7}
print(a, type(a)) # drop duplicated value and sort

a = a - b # 차집합
a = a & b # 교집합
# a = a + b # unsupported operand type 
a = a | b # 합집합
a = a ^ b # 교집합 반대 
"""29. 집합형의 메소드 """
s = {1, 2, 3, 4, 5}
# s[0] 집합은 순서가 없어서 TypeError
s.add(6)
s.remove(6)
s.clear() # 삭제 


"""30. 집합형의 사용 예"""
# 소셜미디어에서 공통점을 찾을 경우 
my_friends = {'A', 'C', 'D'}
A_friends = {'B', 'D', 'E', 'F'}

print(my_friends & A_friends)

# 중복된 과일 삭제 
f = ['apple', 'banana', 'apple', 'banana']
kind = set(f)
print(kind)



