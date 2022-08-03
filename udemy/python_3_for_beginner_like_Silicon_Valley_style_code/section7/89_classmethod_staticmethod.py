class Person(object):
    kind = 'human'
    
    def __init__(self):
        self.x = 100
    
    #1 클래스메서드: 오브젝트 상태가 아닌 클래스의 kind를 가리키는 것이 가능합니다.
    #1 생성하지 않아도 사용 가능합니다.
    @classmethod    
    def what_is_your_kind(self):
        return self.kind

    # 잘 쓰이지 않지만, 이렇게 사용하는 것도 가능하다. 
    @staticmethod
    def about(year):
        print('about human {}'.format(year))

a = Person()
print(a.x) 
b = Person
print(b.x) # Person이 생성되지 않았기 때문에 오류 발생

a = Person()
print(a.kind) 
b = Person
print(b.kind) # 클래스 변수는 사용 가능 