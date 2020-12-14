
class NodoDB:
    def __init__(self,name):
        self.name=name
        self.tables={}
        self.left   = None
        self.right  = None
        self.height = 0   #altura 


    def show(self):
        return print("Data Base ",self.name, "  tabla ",self.tables)

    
    
class DataBase():

    def __init__(self):
        super().__init__()
        self.root=None
    
    def add(self,name,lista):
        self.root=self._add(self.root,name,lista)

    def _add(self,raiz,name,lista):
        

    def showDB(self):
        print("D")

    
    def CreateDB(self,Name):
        


    def DropDB(self,NameDB):
        print("D")
