class Car(object):
    def run(self):
        print('run')

# 차의 기능을 inherit를 함
class ToyotaCar(Car):
    pass

class TeslaCar(Car):
    def auto_run(self):
        print('auto_run')


car = Car()
car.run()

toyota_car = ToyotaCar()
toyota_car.run()

tesla_car = TeslaCar()
tesla_car.run() # Car에 있는 기능을 계승 
tesla_car.auto_run() # TeslaCar의 메서드 

