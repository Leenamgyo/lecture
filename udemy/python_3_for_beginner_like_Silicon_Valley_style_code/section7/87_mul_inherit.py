class Person(object):
    def talk(self):
        print('talk')
        
class Car(object):
    def run(self):
        print('run')

#1 왼쪽이 먼저 계승이 되기 때문에 
#2 메소드가 서로 같은 경우 왼쪽 클래스의 메소드가 사용된다.
#3 이러한 문제가 있어 다중계승을 안쓰는 것이 괜찮다. 
class PersonCarRobot(Person, Car):
    def fly(self):
        print('fly')


