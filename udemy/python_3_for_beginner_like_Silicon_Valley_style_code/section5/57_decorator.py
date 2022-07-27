# 이런 식으로 decorator를 만들 것이야
def add_num(a, b):
    return a + b

print('start')
r = add_num(10, 20)
print('end')
print(r)

# closure의 이론을 이용함 
def print_info(func):
    def wrapper(*args, **kwargs):
        print('start')
        result = func(*args, **kwargs)
        print('end')
        return result
    return wrapper

def print_more(func):
    def wrapper(*args, **kwargs):
        print('func:', func.__name__)
        print('args: ', args)
        print('kwargs:', kwargs)
        result = func(*args, **kwargs)
        print('result:', result)
        return result
    return wrapper

        

def add_num(a, b):
    return a + b

f = print_info(add_num)
r = f(10, 20)
print(r)

# 다른 방식으로 실행하기 
@print_info
def add_num(a, b):
    return a + b

r = add_num(10, 20)
print(r)

# 이러한 방식으로 데코레이터 적용 가능합니다. 
@print_info
def sub_num(a, b):
    return a - b


# print_info(print_more(add_num))
@print_info 
@print_more
def sub_num(a, b):
    return a - b

# print_more(print_info(add_num))

@print_more
@print_info 
def sub_num(a, b):
    return a - b

r = sub_num(10, 20)
print(r)


    