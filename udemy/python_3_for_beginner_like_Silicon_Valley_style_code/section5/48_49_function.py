def say_something():
    print('hi')
    
# 함수를 정의한 뒤에 실행을 할 것 
say_something()
print(type(say_something()))

def say_something():
    print('hi')
    return s
    
result = say_something()

def what_is_this(color):
    if color == 'red'
        return 'tomato'
    elif color == 'green':
        return  'green pepper'
    else:
        return "I don't know"
        
    
result = what_is_this('red') # red
print(result)

## 함수의 인수와 반환값의 선언

num: int = 10
def add_num(a: int, b: int) -> int:
    return a + b

# 애노테이션은 타입 힌트일 뿐 타입을 강제하지 않기 때문에 문자열도 들어갈 수 있다. 
r = add_num('a', 'b')
print(r)

