from unicodedata import name


class Person(object):
    def __init__(self):
        self.name = name
        
    def say_something(self):
        print("I am {}. hello".format(self.name))
        self.run(1)
        
    def run(self, num):
        print('run' * num)
    
person = Person('Mike')
