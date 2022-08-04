import os 
import pathlib
import glob
import shutil

# print (os.path.isdir('desing')) # is directory?
# os.rename('test.txt', 'renamed.txt') # rename
# os.symlink('renamed.txt', 'symlink.txt') # make 바로가기(symbolic link) 파일 

# os.mkdir('test_dir') # create directory
# os.rmdir('test_dir') # remove directory, 하부 내용이 있으면 못 지움 

# pathlib.Path('empty.txt').touch() # linux touch
# os.remove('empty.txt')

# os.mkdir('test_dir')
# os.mkdir('test_dir/test_dir2') 
# print(os.listdir('test_dir')) # test_dir 안에 위치해 있는 directory를 리스트로 내보내줌

shutil.copy('dir/file.txt') # file copy
shutil.rmtree('dir') # dir 아래의 파일을 모두 삭제 
print(glob.glob('test_dir/test_dir2/*')) # directory 안에 어떤 것이 있는지 확인 
print(os.getcwd()) # 파이썬 파일이 있는 dir
