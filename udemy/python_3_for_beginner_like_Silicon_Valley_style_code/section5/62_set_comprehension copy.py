def g():
    for i in range(10):
        yield 1
        
g = g()
g = (i for i in range(10))
print(type(g)) # generator

g = tuple(i for i in range(10)) 
print(type(g)) # tuple
