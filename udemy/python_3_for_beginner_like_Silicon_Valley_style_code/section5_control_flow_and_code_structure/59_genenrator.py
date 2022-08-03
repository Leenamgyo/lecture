# 제네레이터는 '이터레이터'의 요소 
# 이터레이트는 반복처리를 할 떄 리스트를 for loop로 돌리는 것
# 제너레이터는 한 요소를 꺼내서 그것을 생성해나가는 것 

# 예시 1 이터레이터
l = ['Good Morning', 'Good afternoon', 'Good night']
for i in l:
    print(i)


# 예시 2: 제너레이터 사용
def greeting():
    yield 'Good morning'
    yield 'Good afternoon'
    yield 'Good night'
    
for g in greeting():
    print(g)
    
# 제네레이터는 하나씩 요소를 생성함 
g = greeting() # generator object 생성 

print(next(g))
print('@@@@@@@')
print(next(g))
print('@@@@@@@')
print(next(g))

def counter(num=10):
    for _ in range(num):
        yield 'run'

c = counter()
print(next(c))



# 예시 3: 제너레이터 사용 (중간에 오래걸리는 동작이 있을 경우)
def greeting():
    yield 'Good morning' #1. 속도 빠르게 출력 
    for i in range(1000000):
        print(i)
    yield 'Good afternoon' #2. 오래걸리는 로직이 끝난 후 출력
    yield 'Good night' # 속도 빠르게 출력
    
# StopIteration : 제네레이터가 모두 소비된 후 next로 다시 출력시켰을 때 오류 