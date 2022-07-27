#위치 인수, 키워드 인수, 디폴트 인수 

# 디폴트 인수 
def menu(entree='beef', drink='wine', dessert='ice'):
    print(entree)
    print(drink)
    print(dessert)
    
# 키워드 인수 
menu (entree='beef', dessert='ice', drink='beer')


# 디폴트 인수를 쓸 때 주의할 점 
def test_func(x, l=[]):
    l.append(x)
    return l

y = [1, 2, 3]
r = test_func(100, y)
print(r) # [1, 2, 3, 100]

y = [1, 2, 3]
r = test_func(200, y)
print(r) # [1, 2, 3, 200]

r = test_func(100) # [100]
print(r)

r = test_func(100) # [100, 100]
print(r)

# 원래는 100이 하나여야 하지만, 파이썬은 리스트를 디폴트 인수로 사용하면 안된다는 암묵적인 룰이 있습니다.
# 왜냐하면, test_func에 정의한 지점에 딱 한번만 생성하게 되기 때문에
# 다음 참조할 때 이미 만들어진 list를 가져와서 사용한다. 
# 만약 defualt 인수를 사용하고 싶으면

def test_func(x, l=None):
    if l is None:
        l = []
        
    l.append(x)
    return l 

# 이와 같이 사용한다. 