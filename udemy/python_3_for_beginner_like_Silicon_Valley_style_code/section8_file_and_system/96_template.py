from importlib.resources import contents
import string

s = """\

Hi $name.

$contents

Have a good day
"""

t = string.Template(s)
contents = t.substitute(name="Mike", contents='How are you?')
print(contents)

#1 s의 내용을 그대로 txt 파일로 옮겨 사용 가능 
with open('design/email_template.txt') as f:
    t = string.Template(f.read())
    
contents = t.substitute(name="Mike", contents='How are you?')
print(contents)