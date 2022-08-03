

# f.close()를 자동으로 해줌 
# finally 구문 생략
with open('text.txt', 'w') as f:
    f.write('test')
    print('My', 'name', 'is', 'Mike', sep='#', end='!', file=f)
    


