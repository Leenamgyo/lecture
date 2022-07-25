some_list = [1, 2, 3, 4, 5]

i = 0
while i < len(some_list):
    print(some_list[i])
    i += 1
    
for s in 'abcde':
    print(s)
    
for word in ['My', 'name', 'is', 'Mike']:
    if word == 'name':
        break
    
    print(word)
    
for fruit in ['apple', 'banana', 'orange']:
    if fruit == 'banana':
        print('stop eating')
        break
    print(fruit)
    
# break로 안빠지면 else로 실행 
else:
    print('I ate all!')