s= 'adsjfklajsdflkjsadlfjk'

# 직접 default 기능을 만들어 이용하는 방법
d= {}
for c in s:
    if c not in d:
        d[c] = 0
    d[c] += 1
    
print(d)

# setdefault를 이용하는 방법
d= {}
for c in s:
    d.setdefault(c , 0) # 키가 없으면 0을 넣을 것
    d[c] += 1
    
print(d)

from collections import defaultdict

d = defaultdict(int)

for c in s:
    d[c] += 1
    
print(d)
print(d['f'])
