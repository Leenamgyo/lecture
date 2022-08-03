s = 'adsjfasdfs'
print(s.capitalize())

# 파이썬 3에서는 오브젝트라는 것을 안써도 됨
class Person(object):
    def say_something(self):
        print('hello')
        
person = Person()
person.say_something()
