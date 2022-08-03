def menu(**kwargs):
    print(kwargs)
    
menu(entree='beef', drink='coffee')

def menu_2(food, *args, **kwargs):
    print(food)
    print(args)
    print(kwargs)
    
menu_2('banana', 'apple', 'orange', entree='beef', drink='coffee')