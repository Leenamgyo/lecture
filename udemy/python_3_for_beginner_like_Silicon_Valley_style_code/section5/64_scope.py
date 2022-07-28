animal = 'cat'

def f():
    # 로컬 animal
    print(animal)
    animal = 'dog'
    print('after', animal)
    
f()
print(animal) #cat

def f():
    # global animal
    global animal
    animal = 'dog'
    print('after', animal)
    
f()
print(animal) # dog

def f():
    # locals animal
    global animal
    animal = 'dog'
    print('after', locals()) # 로컬 변수 확인
    
f()
print('global', globals()) # 글로벌 변수 확인 

