import abc

class Person(object):
    def __init__(self, age=1):
        self.age = age
    
    #1 추상 메소드 선언
    #2 구체화된 클래스에서 선언하지 않으면 에러 발생
    @abc.abstractclassmethod
    def drive(self):
        pass
    
    def drive(self):
        if self.age >= 18:
            print('ok')
        else:
            raise Exception('No drive')
        
class Baby(Person):
    def __init__(self, age=1):
        if age < 18:
            super().__init__(age)
        else:
            raise ValueError

    def drive(self):
        raise Exception('No drive')
    
class Adult(Person):
    def __init__(self, age=18):
        if age >= 18:
            super().__init__(age)
        else:
            raise ValueError
        
    def drive(self):
        print('ok')
    

baby = Baby()
adult = Adult()

class Car(object):
    def __init__(self, model=None):
        self.model = model
    def run(self):
        print('run')
    def ride(self, person):
        person.drive()

car = Car()
car.ride(adult)


# https://ko.wikipedia.org/wiki/%EB%8D%95_%ED%83%80%EC%9D%B4%ED%95%91
# 객체의 변수 및 메소드의 집합이 객체의 타입을 결정하는 것을 말한다. 
# 클래스 상속이나 인터페이스 구현으로 타입을 구분하는 대신, 덕 타이핑은 객체가 어떤 타입에 걸맞는 변수와 메소드를 지니면 해당 타입에 속하는 것으로 간주한다. 

# 유래 
# 만약 어떤 새가 오리처럼 걷고, 헤엄치고, 꽥꽥거리는 소리를 낸다면 그 새를 오리라고 부를 것이다. 
# 즉, 오리와 유사한 행동을 할 경우 오리라고 간주할 수 있다. 