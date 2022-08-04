import datetime

now = datetime.datetime.now() # 지금
print(now)
print(now.isoformat()) # iso format 
print(now.strftime('%d/%m/%y-%H%M%S%f'))

today = datetime.date.today() # 오늘 날짜
print(today)
print(today.isoformat())
print(now.strftime('%d/%m/%y'))

t = datetime.time(hour=1, minute=10, second=5, microsecond=100) # 직접 
print(t)
print(t.isoformat())

print(now)
d = datetime.timedelta(weeks=-1) 
print(now + d) #  일주일 전으로 시간 돌리기

print(now)
d = datetime.timedelta(weeks=1) 
print(now - d) #  일주일 전으로 시간 돌리기

import time 
print(time.time()) # epochtime , 1509917...
