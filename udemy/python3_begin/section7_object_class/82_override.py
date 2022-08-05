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
    def __init__(self, model='Model S', enable_auto_run=False):
        #1 __init__을 덮어쓰기 때문에 __init__ 또한 override 가 되어 TeslaCar의 __init__으로 바뀐다. 
        #2 만약 super 클래스를 재사용하고 싶으면 super().__init__(model)을 사용하여 기반 클래스의 init을 가져온다.
        
        # self.model = model 
        super().__init__(model) # 기반 클래스의 
        self.enable_auto_run = enable_auto_run
    
    def run(self): # override
        print('super fast')
    
    def auto_run(self):
        print('auto_run')


car = Car()
car.run()

toyota_car = ToyotaCar('Lexus')
toyota_car.run()

tesla_car = TeslaCar('Model S')
tesla_car.run() # Car에 있는 기능을 계승 
tesla_car.auto_run() # TeslaCar의 메서드 

