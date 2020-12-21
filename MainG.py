import os
from DataBaseTree_AVL import *
import shutil
import pickle



data = AVLTree()
    # CRUD DE LA BASE DE DATOS
def dropDatabase( database: str) -> int:
    if verificador(database) == True:
        data.Eliminar(database)
        shutil.rmtree("data/databases/"+database)
        return 0
    elif verificador(database) == False:
        return 2
    else:
        return 1

def createDatabase( database: str) -> int:
    if verificador(database) == True:
        return 2
    elif verificador(database) == False:
        initCheck(database)
        data.add(database)
        
        return 0
    else:
        return 1

def showDatabases() -> list:
    return data.imprimir()

def alterDatabase( databaseOld, databaseNew) -> int:
    if verificador(databaseOld) == False:
        return 2
    elif verificador(databaseNew) == True:
        return 3
    elif verificador(databaseOld):
        data.modicar(databaseOld, databaseNew)
        os.rename('data/databases/'+databaseOld,
                  'data/databases/'+databaseNew)
        return 0
    else:
        return 1

    # CRUD DE LAS TABLAS QUE ESTAN DENTRO DE LA BASE DE DATOS
def createTable( database: str, table: str, numberColumns: int) -> int:
    try:
        if verificador(database) == True:
            return data.bus(database).createTable(table,numberColumns,database)
        else:
            return 2
    except expression as identifier:
        return 1


def showTables( database: str) -> list:
    try:
        if verificador(database):
                # retornar la lista
            contenido = os.listdir('data/databases/'+str(database))
            return contenido
        else:
            return None
    except error:
        return None


def alterTable( database: str, tableOld: str, tableNew: str) -> int:
    try:
        if verificador(database):
            return  data.bus(database).alterTable(tableOld,tableNew,database)
        else:
            return 2
    except error:
        return 1

def dropTable(database: str, table:str) -> int:
    try:
        if verificador(database):
            return data.bus(database).dropTable(table,database)
        else:
            return 2
    except error:
        return 1
        

def alterAddColumn(database: str, table :str) -> int:
    print("agregar columna")
    
def alterDropColumn(database: str, table :str, columnNumber: int) -> int:
    try:
        if verificador(database) == True:
            return data.bus(database).alterDropColumn(table,columnNumber)
        else:
            return 2
    except error:
        return 1

    
def extractTable(database: str, table :str) -> list:
    try:
        if verificador(database):
            return data.bus(database).extractTable(table)
        else:
            return None
    except error:
        return None

    
def extractRangeTable(database: str, table: str, columnNumber: int, lower: any, upper: any) -> list:
    try:
        if verificador(database):
            return data.bus(database).extractRangeTable(table,columnNumber,lower,upper)
        else:
            return None
    except error:
        return None

    # FUNCIONES DENTRO DE LAS TUPLAS
def insert(database: str, table :str, register: list) -> int:
    if verificador(database):
            return data.bus(database).insert(table,register)
    else:
        return 2
    
def update(database: str, table :str, register: dict, columns: list) -> int:
    if verificador(database):
        return data.bus(database).update(table,register,columns)
    else:
        return 2
    
def delete(database: str, table: str, columns: list) -> int:
    try:
        if verificador(database):
            return data.bus(database).delete(table,columns)
        else:
            return 2
    except error:
        return 1

    
def truncate(database: str, table: str) -> int:
    try:
        if verificador(database):
            return data.bus(database).truncate(table,database)
        else:
            return 2
    except error:
        return 1

def alterAddPK(database: str, table: str, columns: list) -> int:
    if verificador(database):
        return data.bus(database).alterAddPK(table,columns)
    else:
        return 1

def alterDropPK(database: str, table: str, columns: list) -> int:
    if verificador(database):
        return data.bus(database).alterDropPK(table,columns)
    else:
        return 2


def loadCSV(file: str, database: str, table: str) -> list:
    try:
        if verificador(database):
            return data.bus(database).loadCSV(file,table)
        else:
            return 2
    except error:
        return 1

    # METODOS EXTRAS 
def initCheck(name):
    if not os.path.exists('data'):
        os.makedirs('data')
    if not os.path.exists('data/databases'):
        os.makedirs('data/databases')
    if not os.path.exists('data/databases/'+str(name)):
        os.makedirs('data/databases/'+str(name))

def verificador(name):
    dum=False
    if os.path.exists('data/databases/'+str(name)):
        dum=True
    return dum
    
def decod(self,ruta):
    file = open(ruta+".bin", "rb")
    b = file.read()
    file.close()
    return pickle.loads(b)
