from ISAM import Indice
from Cilindro import Registro as r
import os
import pickle
import shutil




class TabsStruct:
    def __init__(self, name, cols, ruta):
        # numero de columnas
        self.countCol = cols
        # nombre de la tabla
        self.name = name
        # llaves primarias
        self.pks = []
        # tuplas con estructura de ISAM
        self.tuplas = Indice(self.pks, ruta)  # tambien pasar ruta de la tabla)


class Tables:
    def __init__(self):
        self.Tabs = {}

    def createTable(self, table, numberColumns, ruta):
        if not table in self.Tabs:
            self.initCheck(str(ruta)+"/"+str(table))
            tab = TabsStruct(table, numberColumns, 'data/databases/'+ruta+"/"+str(table))
            self.Tabs[table] = tab
            return 0
        else:
            return 3

    def showTables(self):
        names = []
        for tabs in self.Tabs:
            names.append(self.Tabs[tabs].name)
        return names

    def extractTable(self, table):
        try:
            return self.Tabs[table].tuplas.readAll()
        except:
            return None
        

    def extractRangeTable(self, table, column, lower, upper):
        try:
            return self.Tabs[table].tuplas.readRange(column, lower, upper)
        except:
            return None
        

    # revisar bien
    def alterAddPK(self, table, columns):
        try:
            if table in self.Tabs:
                if len(columns) <= self.Tabs[table].countCol:
                    for x in columns:
                        if not x in self.Tabs[table].pks:
                            self.Tabs[table].pks.append(x)
                            self.Tabs[table].tuplas.pkey=columns
                            self.Tabs[table].tuplas.refreshMem()
                        else:
                            return 4
                    return 0
                else:
                    return 5
            else:
                return 3
        except:
            return 1
        

    def alterDropPK(self, table):
        try:
            if table in self.Tabs:
                if len(self.Tabs[table].pks) != 0:
                    self.Tabs[table].pks = []
                    self.Tabs[table].tuplas.pkey = []
                    return 0
                else:
                    return 4
            else:
                return 3
        except:
            return 1
        

    def alterTable(self, tableOld, tableNew, ruta):
        try:
            if tableOld in self.Tabs:
                if not tableNew in self.Tabs:
                    temp = self.Tabs[tableOld]
                    self.dropTable(tableOld, ruta)
                    self.createTable(tableNew, temp.countCol, ruta)
                    self.Tabs[tableNew].pks = temp.pks
                    self.Tabs[tableNew].tuplas = temp.tuplas
                    return 0
                else:
                    return 4
            else:
                return 3
        except:
            return 1

    def alterAddColumn(self, table, default):
        self.Tabs[table].countCol += 1
        # agregar alter add column de Registro
        return self.Tabs[table]

    def alterDropColumn(self, table, columnNumber):
        if self.Tabs[table].countCol > 0:
            self.Tabs[table].countCol -= 1
            # agregar alter drop column de Registro
            return self.Tabs[table]

    def dropTable(self, table, ruta):
        try:
            if table in self.Tabs:
                del self.Tabs[table]
                shutil.rmtree("data/databases/"+str(ruta)+"/"+str(table))
                return 0
            else:
                return 3
        except:
            return 1

    def insert(self, table, register):
        #try:
            if table in self.Tabs:
                if len(register) == self.Tabs[table].countCol:
                    return self.Tabs[table].tuplas.insert(register)
                else:
                    return 5
            else:
                return 3
        except:
            return 1

    def extractRow(self, table, columns):
        try:
            if table in self.Tabs:
                return self.Tabs[table].tuplas.extractRow(columns)
            else:
                return []
        except:
            return []

    def update(self, table, register, columns):
        try:
            if table in self.Tabs:
                return self.Tabs[table].tuplas.update(register,columns) 
            else:
                return 3
        except:
            return 1

    def delete(self, table, columns):
        try:
            if table in self.Tabs:
                return self.Tabs[table].tuplas.delete(columns)
            else:
                return 3
        except:
            return 1

    def truncate(self, table, ruta):
        try:
            if table in self.Tabs:
                pk = self.Tabs[table].tuplas.pkey
                self.Tabs[table].tuplas = Indice(pk, 'data/databases'+ruta+"/"+str(table))
                return 0
            else:
                return 3
        except:
            return 1

    def loadCSV(self,filepath, table) :
        try:
            res = []
            import csv
            with open(filepath, 'r') as file:
                reader = csv.reader(file, delimiter = ',')
                for row in reader:
                    res.append(self.insert(table,row))
            return res
        except:
            return []

    def initCheck(self, name):
        if not os.path.exists('data/databases/'+name):
            os.makedirs('data/databases/'+name)
