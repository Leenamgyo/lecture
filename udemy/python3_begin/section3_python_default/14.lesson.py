'''14. 문자의 대입'''
word = 'a is {}'.format('a')
print(word)

word = 'a is {}'.format('test')
print(word)

word = 'a is {} {} {} '.format(1, 2, 3)
print(word)

word = 'a is {2} {1} {0} '.format(1, 2, 3)
print(word) # format arg 순서 변경 가능 

word = 'a is {name} {family}. Watashi ha {family} {name}'.format(name='Jun', family= 'Sakai')
print(word) 

# f-format
print(f'a is {word}')
