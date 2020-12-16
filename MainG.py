import os 
from DataBaseTree_AVL import AVLTree 
import shutil

class Main:
    
    def __init__(self):
        self.database= AVLTree()
        
    
    def dropDatabase(self,database: str) -> int: 
        self.database.Eliminar(database)
        shutil.rmtree("data/databases/"+database)
        

    def createDatabase(self,database:str)-> int:
        if self.verificador(database)==True:
            return 2
        elif self.verificador(database)==False:
            self.initCheck(database)
            lista={1:" Me ",2:" llamo ",3:" mynor"}
            self.database.add(database,lista)
            return 0
        else:
            return 1


    def showDatabases(self) -> list:
        self.database.imprimir()
            


    def alterDatabase(self,databaseOld, databaseNew) -> int:
        if self.verificador(databaseOld)==False:
            return 2
        elif self.verificador(databaseNew)==True:
            return 3
        elif self.verificador(databaseOld):
            self.database.modicar(databaseOld,databaseNew)
            os.rename('data/databases/'+databaseOld,'data/databases/'+databaseNew)
            return 0
        else:
            return 1


    def initCheck(self,name):
        if not os.path.exists('data'):
            os.makedirs('data')
        if not os.path.exists('data/databases'):
            os.makedirs('data/databases')
        if not os.path.exists('data/databases/'+name):
            os.makedirs('data/databases/'+name)

    def verificador(self,name):
        dum=False
        if os.path.exists('data/databases/'+name):
            dum=True
        return dum

s=Main()
print(s.createDatabase("base1"))
print(s.createDatabase("base2"))
print(s.createDatabase("base3"))
print(s.createDatabase("base4"))
print(s.createDatabase("base5"))
print(s.createDatabase("base6"))
print(s.createDatabase("base7"))
print(s.dropDatabase("base3"))
print(s.alterDatabase("base7","Holisbase7"))
s.showDatabases()