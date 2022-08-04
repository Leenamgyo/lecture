import tarfile # 압축 및 풀기 

with tarfile.open('test.tar.gz', 'w:gz') as tr: # 타르 파일 생성 
    tr.add('test_dir') 

with tarfile.open('test.tar.gz', 'r:gz') as tr:
    # tr.extractall(path='test_tar') 전체 
    with tr.extractfile('test_dir/sub_dir/sub_test.txt') as f:
        print(f.read()) # 파일 내용만 읽어오는 방법 