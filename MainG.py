import os
from DataBaseTree_AVL import AVLTree
import shutil


class Main:

    def __init__(self):
        self.database = AVLTree()

    # CRUD DE LA BASE DE DATOS
    def dropDatabase(self, database: str) -> int:
        if self.verificador(database) == True:
            self.database.Eliminar(database)
            shutil.rmtree("data/databases/"+database)
            return 0
        elif self.verificador(database) == False:
            return 2
        else:
            return 1

    def createDatabase(self, database: str) -> int:
        if self.verificador(database) == True:
            return 2
        elif self.verificador(database) == False:
            self.initCheck(database)
            lista = {1: " Me ", 2: " llamo ", 3: " mynor"}
            self.database.add(database, lista)
            return 0
        else:
            return 1

    def showDatabases(self) -> list:
        self.database.imprimir()

    def alterDatabase(self, databaseOld, databaseNew) -> int:
        if self.verificador(databaseOld) == False:
            return 2
        elif self.verificador(databaseNew) == True:
            return 3
        elif self.verificador(databaseOld):
            self.database.modicar(databaseOld, databaseNew)
            os.rename('data/databases/'+databaseOld,
                      'data/databases/'+databaseNew)
            return 0
        else:
            return 1

    # CRUD DE LAS TABLAS QUE ESTAN DENTRO DE LA BASE DE DATOS
    def createTable(self, database: str, table: str, numberColumns: int) -> int:
       try:
            if self.verificador(database) == True:
                if self.verificador(str(database)+"/"+str(table)):
                    return 3
                else:
                    self.initCheck(str(database)+"/"+str(table))
                    self.database
                    return 0
            else:
                return 2 
       except expression as identifier:
           return 1

    def alterAddPK(self,database: str, table:str , columns: list) -> int:
        print("AGREGAR LLAVE PRIMARIA")

    def alterDropPK(self,database: str, table:str) -> int:
        print("ELIMINAR LLAVE PRIMARIA")

    def defineFK(self,database: str, table:str, references: dict) -> int:
        #para la fase 2
        print("integridad de las tablas")

    def showTables(self,database: str) -> list:
        try:
            if self.verificador(database):
                #retornar la lista 
                tabs=self.database.tables.showTables(database)
                return tabs
            else:
                return None
        except error:
            return None

    def alterTable(self,database: str, tableOld: str, tableNew: str) -> int:
       try:
            if self.verificador(database):
                if self.verificador(str(database)+"/"+str(tableOld)):
                    if self.verificador(str(database)+"/"+str(tableOld)):
                        return 4
                    else:
                        self.database.tables.alterTable(database,tableOld,tableNew)
                        return 0
                else:
                    return 3
            else:
                return 2
        except error:
            return 1

    def dropTable(self,database: str, table:str) -> int:
        try:
            if self.verificador(database):
                if self.verificador(str(database)+"/"+str(table)):
                    shutil.rmtree("data/databases/"+str(database)+"/"+str(table))
                    return 0
                else:
                    return 3
            else:
                return 2
        except error:
            return 1
        

    def alterAddColumn(self,database: str, table :str) -> int:
        print("agregar columna")
    
    def alterDropColumn(self,database: str, table :str, columnNumber: int) -> int:
        print("elimina columna")

    
    def extractTable(self,database: str, table :str) -> list:
        try:
            if self.verificador(database):
                if self.verificador(str(database)+"/"+str(table)):
                    reg = self.database.tables.extractTable(database,table)
                    return reg
                else:
                    return None
            else:
                return None
        except error:
            return None

    
    def extractRangeTable(self,database: str, table :str, lower: Any, upper: Any) -> list:
        print("entrae una tabla y lo devuelve en lista pero en un rango especifico")

    # FUNCIONES DENTRO DE LAS TUPLAS
    def insert(self,database: str, table :str, register: list) -> int:
        print("ingresa datos")

    
    def update(self,database: str, table :str, register: dict, columns: list) -> int:
        print("inserta dato")

    
    def delete(self,database: str, table: str, columns: list) -> int:
        print("elimina datos de una tabla")

    
    def truncate(self,database: str, table: str) -> int:
        print("elimina un registro")

    
    def extractRow(self,database, table, id): 
        print("extrae y devuelve una tupla especificada")


    # METODOS EXTRAS 
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
print(s.alterDatabase("Holisbase7","Holi"))
s.showDatabases()
