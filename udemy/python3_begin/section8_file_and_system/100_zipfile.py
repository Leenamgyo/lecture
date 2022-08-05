import glob
import zipfile

with zipfile.ZipFile('test.zip', 'w') as z:
    z.write('test_dir')
    z.write('test_dir/test.txt')
    for f in glob.glob('test_dir/**', recursive=True): # ** 전체 하위 *는 하나의 하위 
        print(f)
        z.write(f)
        

with zipfile.ZipFile('test.zip', 'r') as z:
    z.extractall('zzz2')
    with z.open('test_dir/test.txt') as f:
        print(f.read())
