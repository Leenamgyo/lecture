l = ['Mon', 'tue', 'Wed', 'Thu', 'fri', 'sat', 'Sun']

def change_word(words, func):
    for word in words:
        print(func(word))

def sample_func(word):
    return word.capitalize()

change_word(l, sample_func)



# 람다로 변경 (변수 선언 방식)
sample_func = lambda word: word.capitalize()
change_word(l, sample_func)

# 람다로 변경 (변수 선언하지 않는 방식)
change_word(l, lambda word: word.capitalize())
