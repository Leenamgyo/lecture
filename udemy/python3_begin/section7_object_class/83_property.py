 class Car(object):
    def __init__(self, model=None):
        self.model = model
    
    def run(self):
        print('run')

# 차의 기능을 inherit를 함
class ToyotaCar(Car):
    def run(self): # override
        print('fast')

class TeslaCar(Car):
    def __init__(self, model='Model S', 
                 enable_auto_run=False,
                 passwd='123'):
        # self.model = model 
        super().__init__(model) # 기반 클래스의 
        #1 underscore는 private기능을 하지 않지만 암묵적으로 private 이라고 생각한다.
        self._enable_auto_run = enable_auto_run
        #5 self.__enable_auto_run = enable_auto_run 클래스 속성에 access 하는 것을 접근으로 불가능함
        self.passwd = passwd

    #2 읽어올 수 있지만 덮어쓰기는 못함 
    @property
    def enable_auto_run(self):
        return self._enable_auto_run
    
    #3 만약 덮어쓰고 싶으면 
    #4 어떤 조건이 매치할 경우에만 덮어쓰기가 가능합니다. 라는 로직을 만들 때 이러한 로직을 사용합니다. 
    @enable_auto_run.setter
    def enable_auto_run(self, is_enable):
        if self.passwd == '456':
            self._enable_auto_run = is_enable
        else:
            raise ValueError
    
    def run(self): # override
        print('super fast')    
    def auto_run(self):
        print('auto_run')

tesla_car = TeslaCar('Model S', passwd='111')
tesla_car.enable_auto_run = True
print(tesla_car.enable_auto_run)

#1 underscore 의 의미
#2 property 사용법
#3 #4 setter 사용법 
#5 __(underscore *2) 사용법