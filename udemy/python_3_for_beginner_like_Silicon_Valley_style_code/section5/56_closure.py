def outer(a, b):
    
    def inner():
        return a + b
    
    return inner

f = outer(1, 2) # 1 and 2 의 인수가 들어간 inner를 return 
r = f() # inner를 실행하여 a + b를 반환함 
print(r)

# example 2
# 인수 초기화를 변경하여 다른 값을 리턴 받고 싶을 경우 '클로저'를 사용합니다. 
def circle_area_func(pi):
    def circle_area(radius):
        return pi * radius * radius
    
    return circle_area

ca1 = circle_area_func(3.14)
ca2 = circle_area_func(3.141592)

print(ca1(10))
print(ca2(10))


