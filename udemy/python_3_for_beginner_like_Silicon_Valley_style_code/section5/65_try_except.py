l = [1, 2, 3]
i = 5

try:
    l[i]
except IndexError as exc:
    print("Don't worry: {}".format(exc))
except NameError as ex:
    print(ex)
except Exception as ex:
    print('other:{}'.format(ex))
else: # 프로그램이 정상적으로 실행되었을 때 실행  
    print('done')
finally: # 반드시 실행 
    print('clean up')
     
print("last")