def outer(a, b):
    
    # 함수 내부에서 이 내부 함수를 몇번씩 사용할 경우 inner 함수를 만든다. 
    def plus(c, d):
        return c + d
    
    r = plus(a, b)
    print(r)
    
outer(1, 2)