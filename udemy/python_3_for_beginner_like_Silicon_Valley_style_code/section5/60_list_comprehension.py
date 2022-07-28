t = (1, 2, 3, 4, 5)
t2 = (5, 6, 7, 8, 9, 10)

r = []
for i in t:
    r.append(i)
    
print(r)

r = [i for i in t]
r = [i for i in t if i % 2 == 0] # 메모리를 적게 사용, append를 안해도 되니 처리가 빠름 
r = [i * j for i in t for j in t2] # 이중 for 문 
print(r)