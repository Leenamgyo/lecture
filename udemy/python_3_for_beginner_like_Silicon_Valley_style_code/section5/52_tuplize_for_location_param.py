def say_something(word, *args):
    print(f"word={word}")
    for arg in args:
        print(arg)
    
say_something('Hi!', 'Mike', 'Nance')
