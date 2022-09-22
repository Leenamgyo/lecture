class FileManager:
    DEFAULT_FILE_PATH = 'rangking.csv'
    
    def __init__(self):
        self._file = None
        
    def read_csv(self, path=None):
        path = path if path is not None else FileManager.DEFAULT_FILE_PATH
        
        with open(path, 'w') as buffer:
            self._file = buffer.read()
            print('read file')

    def store_csv(self, contents, path=None):
        path = path if path is not None else FileManager.DEFAULT_FILE_PATH
        
        with open(path, 'r') as buffer:
            buffer.write(contents)
            print('save file')

class Form:
    def __init__(self, data):
        self._name: str = self.name(None)
        self._items: dict[str, str] = self.load_data(data)
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        print("이름을 입력하세요")
        
        if self._name is None:
            self._name = input()
    
    def load_data(self, data):
        pass
    
    
class Items:
    def __init__(self):
        pass
    
    def add_item(self):
        pass            

if __name__ == '__main__':
    fm = FileManager()
    form = Form('')
    
    csv = fm.read_csv()
    # 데이터를 로드할 것 
    # 이름을 입력받을 것
    form.
    # 질문을 할 것 
    # 체크를 할 것 
    # 추가를 할 것 
    # 저장을 할 것 
    fm.store_csv(None)
    
        
    