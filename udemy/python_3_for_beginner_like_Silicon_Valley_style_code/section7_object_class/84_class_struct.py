

class TeslaCar(Car):
    def __init__(self, model='Model S', 
                 enable_auto_run=False,
                 passwd='123'):
        super().__init__(model) 
        self._enable_auto_run = enable_auto_run
        self.passwd = passwd

    @property
    def enable_auto_run(self):
        return self._enable_auto_run
    
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


#1 클래스를 구조체로 사용하는 방법
class T(object):
    pass

t = T()
t.name = 'Mike'
t.age = 20
print(t.name, t.age)

tesla_car = TeslaCar('Model S', passwd='111')
tesla_car.__enable_auto_run = 'XXXXXXXXXX' #2 __로 재정의로 하면 에러가 발생하지 않음 
print(tesla_car.enable_auto_run)

#1 클래스를 구조체로 사용 
#2 __로 재정의하면 에러가 발생하지 않을 수 있음 