class UppercaseError(Exception):
    pass


def check():
    words = ['apple', 'orange', 'banana']
    for word in words:
        if word.isupper():
            raise UppercaseError(word)

try: 
    check()
except UppercaseError as exc:
    print('This is my fault. Go next')
except ValueError as err:
    print('This is ValueError')