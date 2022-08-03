class Word(object):
    
    def __init__(self, text):
        self.text = text
        
    def __str__(self):
        return "Word!!!!!!"
    
    def __len__(self):
        return len(self.text)
    
    # + 연산
    def __add__(self, word):
        return self.text.lower() + word.text.lower()
    
    # 기본 __eq__는 id 검사이나 특수메소드를 통해 변경할 수 있음 
    def __eq__(self, word):
        return self.text.lower() == word.text.lower()
    
w = Word('test')
w2 = Word('test')

print(w == w2)

