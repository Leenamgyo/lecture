f = open('text.txt', 'w')
f.write('test')

# 이런식으로도 파일 출력이 가능함 
print('My', 'name', 'is', 'Mike', sep='#', end='!', file=f)
f.close()