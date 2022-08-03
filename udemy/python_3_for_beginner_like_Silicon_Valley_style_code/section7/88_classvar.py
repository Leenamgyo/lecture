class Person(object):
    
    kind = 'human' #1 클래스 변수, 모든 객체가 공유한다.
    
    def __init__(self, name):
        self.kind = 'human'
        self.name = name
        
    def who_are_you(self):
        print(self.name, self.kind)
        
a = Person('A')
a.who_are_you() # A human

b = Person('B')
b.who_are_you() # B human

class T(object):
    words = []
    
    def add_word(self, word):
        self.words.append(word)
        
c = T()
c.add_word('add 1')
c.add_word('add 2')


d = T()
d.add_word('add 3')
d.add_word('add 4')
print(c.words) #2 words가 공유되어 add 1 ~ add 4 까지 나옴


class T(object):
    
    #3 이렇게 멤버변수로 구현할 수 있음 
    def __init__(self) -> None:
        self.words = []
    
    def add_word(self, word):
        self.words.append(word)