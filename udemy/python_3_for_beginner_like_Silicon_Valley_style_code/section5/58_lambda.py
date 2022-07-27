l = ['Mon', 'tue', 'Wed', 'Thu', 'fri', 'sat', 'Sun']

def change_word(words, func):
    for word in words:
        print(func(word))
        

def sample_func(word):
    return word.capitalize()

